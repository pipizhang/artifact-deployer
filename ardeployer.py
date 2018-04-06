#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Jenkins Artifact Deployer """

import sys
import ardeployer.cli

if __name__ == "__main__":
    if not sys.version_info >= (3, 6):
        sys.exit(1)
    ardeployer.cli.run()

