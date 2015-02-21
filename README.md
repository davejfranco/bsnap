
##**BSNAP**###

Deletes 7 days old snapshots and it creates new ones from 'attached' volumes. It will notify via aws sns whether the process success or failed.


## **Requirements:** ##

 - python2.7
 - Boto >= 2.33.0
 - Virtualenv(optional)

## **Usage:** ##

 * Install the script using 'python setup.py install',
 * Add Credentials, region and sns topic on bsnap.conf
 * Create a cron job pointing to the main file.

ENJOY!!!

