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

print '***********************'
print '*  Making Backup      *'
print '***********************'

#Connecting to us_west-region
today = date.today())


#def old_snapshots():

#	snapshots = ec2.get_all_snapshots(filters={'tag:Creation_date':'*'}

#	return snapshots



def get_ec2_volumes(tag_key, tag_value):

	filter = {
		'tag:'+tag_key:tag_value
	}
	volumes = ec2.get_all_volumes(filters=filter)
	return volumes
 
def Backup_volumes():
	
	volumes = get_ec2_volumes('Name', 'qa-www')
	for n in range(len(volumes)):
		if volumes[n].attachment_state() == 'attached':
			for v in volumes:
				v.create_snapshot('Weekly_Backup')
	
	print 'Listo'

Backup_volumes()



