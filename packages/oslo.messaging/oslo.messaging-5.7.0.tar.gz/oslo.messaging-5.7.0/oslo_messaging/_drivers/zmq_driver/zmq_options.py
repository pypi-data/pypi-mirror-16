#    Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import socket

from oslo_config import cfg

from oslo_messaging._drivers import base
from oslo_messaging import server


MATCHMAKER_BACKENDS = ('redis', 'dummy')
MATCHMAKER_DEFAULT = 'redis'


zmq_opts = [
    cfg.StrOpt('rpc_zmq_bind_address', default='*',
               deprecated_group='DEFAULT',
               help='ZeroMQ bind address. Should be a wildcard (*), '
                    'an ethernet interface, or IP. '
                    'The "host" option should point or resolve to this '
                    'address.'),

    cfg.StrOpt('rpc_zmq_matchmaker', default=MATCHMAKER_DEFAULT,
               choices=MATCHMAKER_BACKENDS,
               deprecated_group='DEFAULT',
               help='MatchMaker driver.'),

    cfg.IntOpt('rpc_zmq_contexts', default=1,
               deprecated_group='DEFAULT',
               help='Number of ZeroMQ contexts, defaults to 1.'),

    cfg.IntOpt('rpc_zmq_topic_backlog',
               deprecated_group='DEFAULT',
               help='Maximum number of ingress messages to locally buffer '
                    'per topic. Default is unlimited.'),

    cfg.StrOpt('rpc_zmq_ipc_dir', default='/var/run/openstack',
               deprecated_group='DEFAULT',
               help='Directory for holding IPC sockets.'),

    cfg.StrOpt('rpc_zmq_host', default=socket.gethostname(),
               sample_default='localhost',
               deprecated_group='DEFAULT',
               help='Name of this node. Must be a valid hostname, FQDN, or '
                    'IP address. Must match "host" option, if running Nova.'),

    cfg.IntOpt('rpc_cast_timeout', default=-1,
               deprecated_group='DEFAULT',
               help='Seconds to wait before a cast expires (TTL). '
                    'The default value of -1 specifies an infinite linger '
                    'period. The value of 0 specifies no linger period. '
                    'Pending messages shall be discarded immediately '
                    'when the socket is closed. Only supported by impl_zmq.'),

    cfg.IntOpt('rpc_poll_timeout', default=1,
               deprecated_group='DEFAULT',
               help='The default number of seconds that poll should wait. '
                    'Poll raises timeout exception when timeout expired.'),

    cfg.IntOpt('zmq_target_expire', default=300,
               deprecated_group='DEFAULT',
               help='Expiration timeout in seconds of a name service record '
                    'about existing target ( < 0 means no timeout).'),

    cfg.IntOpt('zmq_target_update', default=180,
               deprecated_group='DEFAULT',
               help='Update period in seconds of a name service record '
                    'about existing target.'),

    cfg.BoolOpt('use_pub_sub', default=True,
                deprecated_group='DEFAULT',
                help='Use PUB/SUB pattern for fanout methods. '
                     'PUB/SUB always uses proxy.'),

    cfg.BoolOpt('use_router_proxy', default=True,
                deprecated_group='DEFAULT',
                help='Use ROUTER remote proxy.'),

    cfg.PortOpt('rpc_zmq_min_port',
                default=49153,
                deprecated_group='DEFAULT',
                help='Minimal port number for random ports range.'),

    cfg.IntOpt('rpc_zmq_max_port',
               min=1,
               max=65536,
               default=65536,
               deprecated_group='DEFAULT',
               help='Maximal port number for random ports range.'),

    cfg.IntOpt('rpc_zmq_bind_port_retries',
               default=100,
               deprecated_group='DEFAULT',
               help='Number of retries to find free port number before '
                    'fail with ZMQBindError.'),

    cfg.StrOpt('rpc_zmq_serialization', default='json',
               choices=('json', 'msgpack'),
               deprecated_group='DEFAULT',
               help='Default serialization mechanism for '
                    'serializing/deserializing outgoing/incoming messages')
]


def register_opts(conf):
    opt_group = cfg.OptGroup(name='oslo_messaging_zmq',
                             title='ZeroMQ driver options')
    conf.register_opts(zmq_opts, group=opt_group)
    conf.register_opts(server._pool_opts)
    conf.register_opts(base.base_opts)
