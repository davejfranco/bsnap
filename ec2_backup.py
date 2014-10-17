#!/usr/bin/env python3
"""
Copyright (C) 2014 Blanclink, Inc.
---------------------------
bsnap: Automatic Instance Snapshot via boto.
Author: Dave Franco <dave.franco@blanclink.com>
---------------------------
bsnap module:
Basically creates snapshots of attached volumes,
checks if there is any old snapshots and deletes it.
"""

import boto.ec2
from datetime import datetime, timedelta

print('***********************')
print('*  Making Backup      *')
print('***********************')


#Connecting to us_west-region
ec2 = boto.ec2.connect_to_region('us-west-2')
Snapshots = ec2.get_all_snapshots(filters={'tag:Name':'*'})

#Delete old Snapshots
def old_snapshots():

    delete_time = datetime.utcnow() - timedelta(7)
    for snapshot in Snapshots:
        start_time = datetime.strptime(snapshot.start_time,'%Y-%m-%dT%H:%M:%S.000Z')
        if start_time < delete_time:
            snapshot.delete()
    return

#Based on volumes attached, create snapshots
def Backup_volumes():
	
    volumes=ec2.get_all_volumes()
    for n in range(len(volumes)):
        if volumes[n].attachment_state()=='attached':
            volumes[n].create_snapshot('Test_Backup')

    return

if __name__=='__main__':
    old_snapshots()
    Backup_volumes()
