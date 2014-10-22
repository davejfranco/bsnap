""" Copyright (C) 2014 Blanclink, Inc.
---------------------------
log module.
Author: Dave Franco <dave.franco@blanclink.com>
---------------------------
Description
Define log message with priority
and send to syslog """
import logging
import logging.handlers

#logger Creation
logger = logging.getLogger('bsnap')
logger.setLevel(logging.INFO)

# create syslog handler and set level to info
handler = logging.handlers.SysLogHandler(address='/dev/log')

# create formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


# add Handler
logger.addHandler(handler)



def info(message):

    return logger.info(message)

def warn(message):

    return logger.warn(message)

def error(message):

    return logger.error(message)

def critical(message):

    return logger.critical(message)



