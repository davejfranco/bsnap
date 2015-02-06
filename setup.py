#!/usr/bin/env python2.7
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

setup(
    name = "bsnap",
    version = "1.2",
    author = "Dave Franco",
    author_email = "dave.franco@blanclink.com",
    description = 'Automatic Snapshots',
    license = "Blanclink, Inc",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bsnap = bsnap.app:main',
        ],
    },
    install_requires = [
        'boto >= 2.33.0'
    ],
    long_description='bsnap deletes 14 days old snapshots '
                     'and creates snapshots every week',
)