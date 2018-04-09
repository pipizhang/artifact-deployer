#!/usr/bin/env python
import os
import sys
import getopt
from texttable import Texttable
from typing import List, Optional
from .jenkins import *
from .config import config_load
from .command import RunCommand, ListCommand

VERSION = '1.0'

class CLI:
    def help_usage(self) -> str:
        return ('Usage: ardeployer.py subcommand [options] [args]\n'
                '\n'
                'Options:\n'
                '  -h, --help           show help message\n'
                '  -v, --version        show version\n'
                'Subcommands:\n'
                '  run                  start deployment\n'
                '  list                 list latest builds\n'
                )

    def help_command(self) -> None:
        print(self.help_usage())
        sys.exit(0) 
    def version_command(self) -> None:
        print('artifact-deployer/{}'.format(VERSION))
        sys.exit(0)

    def run_command(self, args: List[str]) -> None:
        RunCommand.execute()

    def list_command(self, args: List[str]) -> None:
        print("sfsd")
        ListCommand.execute()

    def process(self, argv: List[str]) -> None:
        config_load()

        try:
            opts, args = getopt.getopt(argv, "hv ", ['help', 'version'])
        except getopt.GetoptError:
            self.help_command()
        for opt, arg in opts:
            if opt in ['-h', '--help']:
                self.help_command()
            if opt in ['-v', '-V', '--version']:
                self.version_command()
        if len(args):
            if args[0] == 'run':
                self.run_command(args[1:])
            elif args[0] == 'list':
                self.list_command(args[1:])
            else:
                self.help_command()
        else:
            self.help_command()


def run(argv: Optional[List[str]]=None) -> None:
    if argv is None:
        argv = sys.argv
    CLI().process(argv[1:])


