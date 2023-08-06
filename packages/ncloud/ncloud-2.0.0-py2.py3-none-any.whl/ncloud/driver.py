# ----------------------------------------------------------------------------
# Copyright 2015-2016 Nervana Systems Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------
"""
Command-line client for interfacing with the Nervana Cloud platform.
"""
from ncloud.vendor.python.argparse import ArgumentParser
from ncloud.vendor.python.argparse import ArgumentDefaultsHelpFormatter

from ncloud.vendor.argcomplete import argcomplete

from ncloud import __version__
from ncloud.config import CMD_NAME, Config
from ncloud.commands import dataset, model, interact, stream, batch, resource
from ncloud.commands.upgrade import Upgrade
from ncloud.commands.configure import Configure


def build_parser(conf):
    parser = ArgumentParser(description=__doc__, prog=CMD_NAME,
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--host", default=conf.get_default_host(),
                        help="Nervana cloud host to connect to.")
    parser.add_argument("--api-ver", default=conf.get_default_api_ver(),
                        help="Nervana cloud API version to use.")
    parser.add_argument("--auth-host",
                        default=conf.get_default_auth_host(),
                        help="Nervana host to connect to to perform "
                             "authorization.")
    parser.add_argument("--tenant", default=conf.get_default_tenant(),
                        help="Tenant name to use for requests.")

    subparser = parser.add_subparsers(title="actions")

    Configure.parser(subparser)

    dataset.parser(subparser)
    model.parser(subparser)
    interact.parser(subparser)
    stream.parser(subparser)
    batch.parser(subparser)
    resource.parser(subparser)

    Upgrade.parser(subparser)

    argcomplete.autocomplete(parser)

    return parser


def main():
    # import sys
    # print(sys.argv[1:])

    conf = Config()
    parser = build_parser(conf)
    args = parser.parse_args()

    # in python3 argparse subparsers are.... optional :/
    # this is the only time func would not be set
    if not getattr(args, 'func', None):
        parser.error('too few arguments')

    conf.set_default_host(args.host)
    conf.set_default_auth_host(args.auth_host)
    conf.set_default_tenant(args.tenant or '')
    conf.set_default_api_ver(args.api_ver)

    args.func(conf, args)
