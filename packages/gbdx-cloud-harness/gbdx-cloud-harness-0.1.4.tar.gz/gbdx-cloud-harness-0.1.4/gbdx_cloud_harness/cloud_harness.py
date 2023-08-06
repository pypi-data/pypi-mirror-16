#!/usr/bin/python
"""
Command Line interface for running remote workflows from client workstations

Usage:
    cloud-harness create <dir_name> [--destination=<path>]
    cloud-harness run <file_name> [--remote] [--verbose] [--upload] [--download] [--dry-run]

Options:
    --verbose           List all the details pertaining.
    --remote            Run the application on the configured environment
    --destination=<path>       Override the location where the application will be created
    --upload            Uploads all the local task ports to S3.
    --download          Downloads the output ports to the local filesystem.
    --dry-run           Do not execute the task.

"""
"""
Notes:

- Default behaviour:
    1) If app is ran LOCALLY,
        then run on local data or raise file not found error.
    2) If app is ran REMOTELY and upload flag is provided,
        push ports data to S3, substitute in workflow value.
    3) If app is ran REMOTELY and NO upload flag,
        Only push source bundle, substitute in workflow. Assumed other port
        values are valid S3 locations. Validate

"""
from docopt import docopt
import imp
import inspect
import os
import sys
import time
import warnings
import tarfile
import shutil
import itertools
import logging
from datetime import datetime

from task_template import TaskTemplate
from services.port_service import PortService
from services.task_service import TaskService
from utils.printer import printer

from gbdxtools import Interface

__author__ = 'michaelconnor'


class TaskController(object):

    RESOURCE_NAME = 'app'

    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

    TEMPLATE_FILENAME = 'task_template.py'

    SOURCE_BUNDLE_PORT = 'source_bundle'

    DEFAULT_NEW_APP_FILENAME = 'app.py'

    IGNORE_FILES_NAME = 'pkg_ignore'

    def __init__(self, arguments):

        self._arguments = arguments

        self.FUNCTION_KEYS = {
            'create': self._create_app,
            'run': self._run_app,
        }

    def invoke(self):
        """
        Execute the command from the arguments.
        :return: None or Error
        """
        for key in self.FUNCTION_KEYS.keys():
            if self._arguments[key] is True:
                self.FUNCTION_KEYS[key]()

    def _create_app(self):
        """
        Method for creating a new Application Template.
        USAGE: cloud-harness create <dir_name> [--destination=<path>]
        """
        template_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), self.TEMPLATE_FOLDER, self.TEMPLATE_FILENAME
        )

        new_dir = self._arguments['<dir_name>']

        # Make new application directory
        override_destination = self._arguments.get('--destination', None)
        if override_destination is not None:
            if override_destination == '':
                raise ValueError('Destination path is empty')
            # Check if the new destination is abs and exists.
            if os.path.isabs(override_destination) and os.path.isdir(override_destination):
                new_dir = os.path.join(override_destination, new_dir)
            else:
                # Create a path from the cwd, then check if it is valid and exists.
                override_path = os.path.join(os.getcwd(), override_destination)
                if not os.path.isabs(override_path) or not os.path.isdir(override_path):
                    raise ValueError('New path parameter %s is not a directory' % override_path)
                new_dir = os.path.join(override_path, new_dir)

        else:
            if os.path.isabs(new_dir) or os.path.sep in new_dir:
                raise ValueError("Directory name is invalid")
            # No override, put the folder in the cwd.
            new_dir = os.path.join(os.getcwd(), new_dir)

        os.makedirs(new_dir)

        new_file_path = os.path.join(new_dir, self.DEFAULT_NEW_APP_FILENAME)

        # Copy the template the new application location.
        shutil.copyfile(template_path, new_file_path)

        printer('New Application created at %s' % new_file_path)

    def _run_app(self):
        """
        Method for running a custom Application Templates.
        NOTES:
            * The default name of the application is app.py. So this function is going to look
            for app.py, unless the --file option is provide with a different file name.
            * The generated source bundle will package everything in the work_path. If large files
            not required for the application source, they need to be ignored. Use a file called "pkg_ignore"
            to identify folders and files to ignore.
        USAGE: cloud-harness run <file_name> [--remote] [--verbose] [--upload] [--download]
        """
        is_remote_run = self._arguments.get('--remote')
        filename = self._arguments.get('<file_name>')
        upload_ports = self._arguments.get('--upload')
        download_ports = self._arguments.get('--download')
        is_verbose = self._arguments.get('--verbose')
        is_dry_run = self._arguments.get('--dry-run')

        if download_ports:  # TODO temporary until implemented.
            raise NotImplementedError("Downloading of output ports is not implemented yet.")

        template_file = self._get_template_abs_path(filename)

        if not os.path.isfile(template_file):
            raise ValueError('The location %s does not exist' % template_file)

        with warnings.catch_warnings():
            # suppress warning from importing
            warnings.filterwarnings("ignore", category=RuntimeWarning)
            template_module = imp.load_source('module.name', template_file)

        template_class = None

        # Find the subclass of TaskTemplate
        for name, data in inspect.getmembers(template_module, inspect.isclass):
            if issubclass(data, TaskTemplate) and data.__name__ != TaskTemplate.__name__:
                template_class = data

        with template_class() as template:
            if is_remote_run:
                task = template.task

                # Create a task service object
                task_service = TaskService()
                printer(task_service.delete_task(task.name))
                printer(task_service.register_task(task.json()))

                task.run_name = '{timestamp}_{task_name}'.format(
                    task_name=task.name,
                    timestamp=datetime.utcnow().strftime('%Y_%m_%d_%H')
                )

                # Create source bundle to be executed on the GBDX platform
                self._archive_source(os.getcwd(), task.src_path)

                port_service = PortService(task)

                if upload_ports:
                    # Push all port data to S3
                    port_service.upload_input_ports()
                else:
                    # Only push source bundle port
                    port_service.upload_input_ports(port_list=[self.SOURCE_BUNDLE_PORT])

                # Build task json to run remotely
                new_task = port_service.task

                # Validate task
                task.is_valid(remote=True)

                workflow = self._get_gbdx_workflow_interface(new_task)

                if is_verbose:
                    printer(template.task.json())

                    temp_wf = self._build_workflow_def_from_interface(workflow)

                    printer(temp_wf)

                if is_dry_run:
                    # Return without executing or monitoring the workflow.
                    return None

                try:
                    printer(workflow.execute())
                except Exception as e:
                    printer(e.message)
                    return

                # Monitor events of workflow
                self.monitor_workflow(workflow)

                if download_ports:
                    # port_service.download_output_port()
                    pass

                # Delete task after run
                printer(task_service.delete_task(task.name))

            else:
                # Validate task
                template.task.is_valid()

                if is_verbose:
                    printer(template.task.json())
                    all_ports = template.task.ports[0] + template.task.ports[1]
                    printer([port.__str__() for port in all_ports])

                if is_dry_run:
                    return

                # Run Task Locally
                try:
                    template.invoke()
                except Exception as e:
                    template.reason = "Failed Exception: %s" % e

                template.reason = "Execution Completed"

    @staticmethod
    def _get_gbdx_workflow_interface(task, session=None):
        if session is None:
            gbdx_interface = Interface()
        else:
            gbdx_interface = Interface(gbdx_connection=session)

        # Override Logger
        hands = gbdx_interface.logger.handlers
        gbdx_interface.logger.addHandler(logging.NullHandler())
        gbdx_interface.logger.removeHandler(hands[0])

        # Create gbdxtools Task and add inputs
        input_ports = {port.name: port.value for port in task.input_ports}
        gbdx_task = gbdx_interface.Task(task.name, **input_ports)

        gbdx_wf = gbdx_interface.Workflow([gbdx_task])

        for port in task.output_ports:
            # Add save data locations
            if port.stageToS3:
                location = '{run_name}/{port}'.format(
                    run_name=task.run_name,
                    port=port.name
                )
                gbdx_wf.savedata(gbdx_task.get_output(port.name), location)

        return gbdx_wf

    @staticmethod
    def _build_workflow_def_from_interface(workflow_obj):

        temp_wf = {"name": workflow_obj.name, "tasks": []}

        for task in workflow_obj.tasks:
            temp_wf['tasks'].append(task.generate_task_workflow_json())

        return temp_wf

    @staticmethod
    def _get_template_abs_path(filename):
        """
        Return a valid absolute path. filename can be relative or absolute.
        """
        if os.path.isabs(filename) and os.path.isfile(filename):
            return filename
        else:
            return os.path.join(os.getcwd(), filename)

    @staticmethod
    def _archive_source(source_folder, destination):

        write_mode = 'w:gz'

        global ignore_location
        ignore_location = source_folder

        if not os.path.isabs(destination) and not os.path.isdir(destination):
            raise ValueError("Invalid destination folder %s" % destination)

        new_dest_filename = os.path.join(destination, 'archive.tar.gz')

        try:
            os.makedirs(destination)
        except OSError as e:
            if 'File exists' in e.message:
                shutil.rmtree(destination)

        with tarfile.open(new_dest_filename, write_mode) as src_archive:
            src_archive.add(source_folder, arcname="", filter=TaskController._filter_archive)

    @staticmethod
    def _filter_archive(tarinfo):

        ignore_filename = os.path.join(ignore_location, TaskController.IGNORE_FILES_NAME)

        if TaskController.SOURCE_BUNDLE_PORT in tarinfo.name:
            return None

        if not os.path.isfile(ignore_filename):
            return tarinfo

        with open(ignore_filename, 'rb') as f:
            for ignore in f.readlines():
                # Only check if the ignore is a folder (startswith) or an extension (endswith)
                ignore = ignore.rstrip().rstrip(os.path.sep)
                if tarinfo.name.startswith(ignore) or tarinfo.name.endswith(ignore):
                    return None

            return tarinfo

    @staticmethod
    def monitor_workflow(workflow):
        """
        Monitor the workflows events and display spinner while running.
        :param workflow: the workflow interface
        """

        spinner = itertools.cycle(['-', '/', '|', '\\'])

        while not workflow.complete:
            for i in xrange(300):
                sys.stdout.write(spinner.next())
                sys.stdout.flush()
                sys.stdout.write('\b')
                time.sleep(0.03)

        if workflow.succeeded:
            sys.stdout.write("\nWorkflow completed successfully\n")
        else:
            sys.stdout.write("\nWorkflow failed: %s\n" % workflow.status)


def main():
    arguments = docopt(__doc__)
    app = TaskController(arguments)
    app.invoke()


if __name__ == '__main__':
    main()
