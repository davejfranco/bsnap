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
import log
import boto.ec2
from datetime import datetime, timedelta


#Connecting to us_west-region
ec2 = boto.ec2.connect_to_region('us-west-2')

"""
This function retrieves all snapshots on the us-west-2
region and catch the start_time attribute, if is 14 days
older than the actual date are going to be deleted.
"""
def OldSnapshots():

    Snapshots = ec2.get_all_snapshots(filters={'tag:Name':'*'})
    delete_time = datetime.utcnow() - timedelta(14)
    for snapshot in Snapshots:
        start_time = datetime.strptime(snapshot.start_time,'%Y-%m-%dT%H:%M:%S.000Z')
        if start_time < delete_time:
            try:
                log.info('Deleting old Snapshots...')
                snapshot.delete()
            except:
                log.error('Unable to delete snapshots')
            else:
                log.error('Successful snapshot delete')
    return
"""
Retrieve all the volumes in the us-west-2 region and
it will create a snapshot only if the volumes is
attached to an instance.
"""
def BackupVolumes():
	
    try:
        log.info('Creating Snapshots...')
        volumes=ec2.get_all_volumes()
        for n in range(len(volumes)):
            if volumes[n].attachment_state()=='attached':
                volumes[n].create_snapshot('Weekly Backup')
    except:
        log.error('Unable to create snapshots')
    else:
        log.info('Successful snapshot creation')

    return

if __name__=='__main__':
    OldSnapshots()
    BackupVolumes()
