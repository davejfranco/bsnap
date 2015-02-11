"""
Copyright (C) Blanclink, Inc.
---------------------------
bsnap: Automatic Instance Snapshots via boto.
Author: Dave Franco <dave.franco@blanclink.com>
---------------------------
bsnap module:
Basically creates snapshots of attached volumes,
checks if there are any old snapshots and deletes them.
"""


import sys
import log
import boto.ec2
import boto.sns
from datetime import datetime, timedelta

# Connecting to us_west-region
ec2 = boto.ec2.connect_to_region('us-west-2')
sns = boto.sns.connect_to_region('us-west-2')

def DeleteSnap(ec2):
    """
    Retrieves all snapshots on the us-west-2
    region and catch the start_time attribute, if is 7 days
    older than the actual date are going to be deleted.
    """

    Snapshots = ec2.get_all_snapshots(filters={'tag:Name':'*'})
    delete_time = datetime.utcnow() - timedelta(7)
    
    try:
        log.info('Deleting old Snapshots...')
        for snapshot in Snapshots:
            start_time = datetime.strptime(snapshot.start_time,
                                       '%Y-%m-%dT%H:%M:%S.000Z')
            if start_time < delete_time:
                snapshot.delete(dry_run=True)
    except:
        log.error('Unable to delete snapshots')
        return False
    else:
        log.info('Successful snapshot delete')
        return True
    
def BackupVol(ec2):
    """
    Retrieve all the volumes in the us-west-2 region and
    it will create a snapshot only if the volumes is
    attached to an instance.
    """
    
    try:
        log.info('Creating Snapshots...')
        volumes=ec2.get_all_volumes()
        for v in volumes:
            if v.status()=='in-use':
                v.create_snapshot(dry_run=True)
    except:
        log.error('Unable to create snapshots')
        return False
    else:
        log.info('Successful snapshot creation')
        return True
    
def main():
    """Main entry point"""
    topic = arn_topic
    subject = "bsnap Backup"
    msg_win = "Successful bsnap Operation"
    msg_fail = "Failed bsnap Operation, check syslog entries"

    if DeleteSnap(ec2) == True and BackupVol(ec2) == True:
        sns.publish(topic, msg_win, subject)

    else:
        sns.publish(topic, msg_fail, subject)

if __name__=='__main__':
    sys.exit(main())
