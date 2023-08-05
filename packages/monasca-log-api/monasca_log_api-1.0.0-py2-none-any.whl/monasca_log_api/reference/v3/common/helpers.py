# Copyright 2014 Hewlett-Packard
# Copyright 2015 Cray Inc. All Rights Reserved.
# Copyright 2016 Hewlett Packard Enterprise Development Company LP
# Copyright 2016 FUJITSU LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import falcon
from monasca_common.rest import utils as rest_utils
from oslo_log import log

LOG = log.getLogger(__name__)


def read_json_msg_body(req):
    """Read the json_msg from the http request body and return them as JSON.

    :param req: HTTP request object.
    :return: Returns the metrics as a JSON object.
    :raises falcon.HTTPBadRequest:
    """
    try:
        msg = req.stream.read()
        json_msg = rest_utils.from_json(msg)
        return json_msg
    except ValueError as ex:
        LOG.debug(ex)
        raise falcon.HTTPBadRequest('Bad request',
                                    'Request body is not valid JSON')
