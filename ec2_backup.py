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
Snapshots = ec2.get_all_snapshots(filters={'tag:Name':'snap_*'})

#Delete old Snapshots
def old_snapshots():

    delete_time = datetime.utcnow() - timedelta(14)
    for snapshot in Snapshots:
        start_time = datetime.strptime(snapshot.start_time,'%Y-%m-%dT%H:%M:%S.000Z')
        if start_time < delete_time:
            snapshot.delete()
        print('Done')


def Backup_volumes():
	
	volumes=ec2.get_all_volumes(filters={'tag:Name':''})
	for n in range(len(volumes)):
		if volumes[n].attachment_state()=='attached':
			for v in volumes:
				v.create_snapshot('Weekly_Backup')

	print ('Listo')

#Backup_volumes()
old_snapshots()


