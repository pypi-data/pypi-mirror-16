# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

from qingcloud.cli.iaas_client.actions.base import BaseAction
from qingcloud.cli.misc.utils import explode_array

class DeleteLoadBalancerListenersAction(BaseAction):

    action = 'DeleteLoadBalancerListeners'
    command = 'delete-loadbalancer-listeners'
    usage = '%(prog)s -s <lb_listeners> [-f <conf_file>]'
    description = 'Delete one or more load balancer listeners'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--lb_listeners', dest='lb_listeners',
                action='store', type=str, default='',
                help='the comma separated IDs of listeners you want to delete.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'lb_listeners': options.lb_listeners,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'loadbalancer_listeners': explode_array(options.lb_listeners),
                }
