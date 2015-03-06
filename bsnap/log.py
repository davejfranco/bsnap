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

"""
Each function refers to
a state of alert which can be use
to send log notification to syslog according to a
specific situation.
"""


def info(message):
    return logger.info(message)

def warn(message):
    return logger.warn(message)

def error(message):
    return logger.error(message)

def critical(message):
    return logger.critical(message)



