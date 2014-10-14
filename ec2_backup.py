#!/usr/bin/env python3

import boto.ec2
from datetime import datetime, timedelta

print '***********************'
print '*  Making Backup      *'
print '***********************'

#Connecting to us_west-region
ec2 = boto.ec2.connect_to_region('us-west-2')
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



