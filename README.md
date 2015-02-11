
##**BSNAP**###

Deletes 7 days old snapshots and it creates new ones from 'in-use' volumes.
It will notify via aws sns whether if the process success or failed


## **Requirements:** ##

 - python2.7
 - Boto >= 2.33.0
 - Virtualenv

## **Usage:** ##

Install the script using 'python setup.py install',
create a cron job pointing to the main file.

For security reasons the script doesn't provide any 
credential information, instead you should either
have the key in a config file or installing the script in a
instance with an IAM role. 