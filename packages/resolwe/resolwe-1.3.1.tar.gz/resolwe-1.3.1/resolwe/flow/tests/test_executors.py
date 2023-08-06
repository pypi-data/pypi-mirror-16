# pylint: disable=missing-docstring
from __future__ import absolute_import, division, print_function, unicode_literals

import mock
import os
import shlex
import six
import subprocess
import unittest

from django.conf import settings
from django.test import override_settings

from resolwe.flow.executors.docker import FlowExecutor
from resolwe.flow.executors import BaseFlowExecutor
from resolwe.flow.models import Data
from resolwe.flow.utils.test import ProcessTestCase

try:
    import builtins  # py3
except ImportError:
    import __builtin__ as builtins  # py2


PROCESSES_DIR = os.path.join(os.path.dirname(__file__), 'processes')


def check_docker():
    """Check if Docker is installed and working.

    :return: tuple (indicator of the availability of Docker, reason for
             unavailability)
    :rtype: (bool, str)

    """
    command = getattr(settings, 'FLOW_EXECUTOR', {}).get('COMMAND', 'docker')
    info_command = '{} info'.format(command)
    available, reason = True, ""
    # TODO: use subprocess.DEVNULL after dropping support for Python 2
    with open(os.devnull, 'wb') as DEVNULL:
        try:
            subprocess.check_call(shlex.split(info_command), stdout=DEVNULL, stderr=subprocess.STDOUT)
        except OSError:
            available, reason = False, "Docker command '{}' not found".format(command)
        except subprocess.CalledProcessError:
            available, reason = (False, "Docker command '{}' returned non-zero "
                                        "exit status".format(info_command))
    return available, reason


class DockerExecutorTestCase(unittest.TestCase):

    @unittest.skipUnless(*check_docker())
    @mock.patch('os.mkdir')
    @mock.patch('os.chmod')
    @mock.patch('os.chdir')
    @mock.patch('resolwe.flow.executors.Data.objects.filter')
    @mock.patch('resolwe.flow.executors.Data.objects.get')
    def test_run_in_docker(self, data_get_mock, data_filter_mock, chdir_mock, chmod_mock, mkdir_mock):
        executor_settings = settings.FLOW_EXECUTOR
        executor_settings['CONTAINER_IMAGE'] = 'centos'

        with override_settings(FLOW_EXECUTOR=executor_settings):
            executor = FlowExecutor()

            script = 'if grep -Fq "docker" /proc/1/cgroup; then echo "Running inside Docker"; ' \
                    'else echo "Running locally"; fi'

            count = {'running': 0}

            def assert_output(line):
                if line.strip() == 'Running inside Docker':
                    count['running'] += 1

            write_mock = mock.MagicMock(side_effect=assert_output)
            stdout_mock = mock.MagicMock(write=write_mock)
            open_mock = mock.MagicMock(side_effect=[stdout_mock, mock.MagicMock()])
            with mock.patch.object(builtins, 'open', open_mock):
                executor.run('no_data_id', script, verbosity=0)

            self.assertEqual(count['running'], 1)


class GetToolsTestCase(unittest.TestCase):
    @mock.patch('resolwe.flow.executors.apps')
    @mock.patch('resolwe.flow.executors.os')
    @mock.patch('resolwe.flow.executors.settings')
    def test_get_tools(self, settings_mock, os_mock, apps_mock):
        apps_mock.get_app_configs.return_value = [
            mock.MagicMock(path='/resolwe/test_app1'),
            mock.MagicMock(path='/resolwe/test_app2'),
        ]
        os_mock.path.join = os.path.join
        os_mock.path.isdir.side_effect = [False, True]
        settings_mock.RESOLWE_CUSTOM_TOOLS_PATHS = ['/custom_tools']

        base_executor = BaseFlowExecutor()
        tools_list = base_executor.get_tools()

        self.assertEqual(len(tools_list), 2)
        self.assertIn('/resolwe/test_app2/tools', tools_list)
        self.assertIn('/custom_tools', tools_list)

    @mock.patch('resolwe.flow.executors.apps')
    @mock.patch('resolwe.flow.executors.settings')
    def test_not_list(self, settings_mock, apps_mock):
        apps_mock.get_app_configs.return_value = []
        settings_mock.RESOLWE_CUSTOM_TOOLS_PATHS = '/custom_tools'

        base_executor = BaseFlowExecutor()
        with six.assertRaisesRegex(self, KeyError, 'setting must be a list'):
            base_executor.get_tools()


class SpawnedProcessTest(ProcessTestCase):
    def setUp(self):
        super(SpawnedProcessTest, self).setUp()
        self._register_schemas(path=[PROCESSES_DIR])

    def test_test(self):
        self.run_process('test-spawn-new')

        data = Data.objects.last()
        data_dir = settings.FLOW_EXECUTOR['DATA_DIR']
        file_path = os.path.join(data_dir, str(data.pk), 'foo.bar')
        self.assertEqual(data.output['saved_file']['file'], 'foo.bar')
        self.assertTrue(os.path.isfile(file_path))
