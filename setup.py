#!/usr/bin/env python2.7
"""
Copyright (c) Dave Franco

Snappy: AWS tool to automate snapshot from volumes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---------------------------
setup module
"""
import os
from setuptools import setup, find_packages

setup(
    name = "snappy",
    version = "1.2",
    author = "Dave Franco",
    author_email = "davefranco1987@gmail.com",
    description = 'Automatic Snapshots',
    license = "Zlib",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'snappy = snappy.app:main',
        ],
    },
    install_requires = [
        'boto >= 2.33.0'
    ],
    long_description='snappy deletes 14 days old snapshots '
                     'and creates snapshots every week',
)