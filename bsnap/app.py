"""
Copyright (c) Dave Franco

bsnap: AWS tool to automate snapshot from volumes

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
Main module
"""

import os
import sys
import log
import boto.ec2
import boto.sns
import ConfigParser
from datetime import datetime, timedelta


config = ConfigParser.ConfigParser()
config.read(os.getcwd()+'/etc/bsnap.conf')
region = config.get('Region','region')
key_id = config.get('Credentials','aws_access_key_id')
secret_key = config.get('Credentials','aws_secret_access_key')

# Connecting to region
ec2 = boto.ec2.connect_to_region(region,aws_access_key_id=key_id,
    aws_secret_access_key=secret_key)
sns = boto.sns.connect_to_region(region,aws_access_key_id=key_id,
    aws_secret_access_key=secret_key)

def DeleteSnap(ec2):
    """
    Retrieves all snapshots on the region
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
        for v in range(len(volumes)):
            if volumes[v].attachment_state()=='attached':
                volumes[v].create_snapshot(dry_run=True)
    except:
        log.error('Unable to create snapshots')
        return False
    else:
        log.info('Successful snapshot creation')
        return True
    
def main():
    """Main entry point"""
    topic = config.get('Sns','arn_topic')
    subject = "bsnap Backup"
    msg_win = "Successful bsnap Operation"
    msg_fail = "Failed bsnap Operation, check syslog entries"

    if DeleteSnap(ec2) == True and BackupVol(ec2) == True:
        sns.publish(topic, msg_win, subject)

    else:
        sns.publish(topic, msg_fail, subject)

if __name__=='__main__':
    sys.exit(main())
