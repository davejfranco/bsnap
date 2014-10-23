#!/usr/bin/env python3
"""
Copyright (C) 2014 Blanclink, Inc.
---------------------------
bsnap: Automatic Instance Snapshot via boto.
Author: Dave Franco <dave.franco@blanclink.com>
---------------------------
setuptools config file
"""
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bsnap",
    version = "1.0",
    author = "Dave Franco",
    author_email = "dave.franco@blanclink.com",
    description = 'Automatic Snapshots',
    license = "Blanclink, Inc",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bsnap = bsnap.app',
        ],
    },
    install_requires = [
        'boto >= 2.33.0'
    ],
    long_description='bsnap deletes 14 days old snapshots and creates snapshots every week',
)