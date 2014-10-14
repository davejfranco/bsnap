#!/usr/bin/env python3
"""
Copyright (C) 2014 Blanclink, Inc.
---------------------------
Author: Dave Franco <dave.franco@blanclink.com>
---------------------------
connector module:
It's in charge of provide aws credentials to
 connect to an specific account
"""
import boto


def connect():

    ec2 = boto.connect_ec2(aws_access_key_id=AKIAIX5DLECFFA6FNH4Q, aws_secret_access_key=vr4DrzBYgwzCjDlTeLW5KROjvgKmVUSXYqCm+a1)

    region = boto.ec2.connect_to_region('us-west-2')

    return




