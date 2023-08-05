# Copyright 2016 FUJITSU LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock
import unittest

from monasca_log_api.reference.v3 import logs


class TestLogsVersion(unittest.TestCase):

    @mock.patch('monasca_log_api.reference.v3.logs.log_publisher'
                '.LogPublisher')
    def test_should_return_v3_as_version(self, _):
        logs_resource = logs.Logs()
        self.assertEqual('v3.0', logs_resource.version)
