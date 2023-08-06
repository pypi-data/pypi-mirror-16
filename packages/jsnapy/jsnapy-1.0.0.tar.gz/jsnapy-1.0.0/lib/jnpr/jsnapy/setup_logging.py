#!/usr/bin/python

# Copyright (c) 1999-2016, Juniper Networks Inc.
#
# All rights reserved.
#

import os
import yaml
import logging.config


def setup_logging(
        default_path='logging.yml', default_level=logging.INFO, env_key='LOG_CFG'):
    path = os.path.join('/etc', 'jsnapy', default_path)
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
