#!/usr/bin/env python3

import sys
import email.utils
import os
import yaml
from common.option import options
from conf import load
import datetime
# Parse options and fetch defaults from git
optsobj = options()
parameters = optsobj.getparameters()
opts = optsobj.parseoptions(sys.argv, parameters)

# get the contents of the yaml file
changes = load.load.getchanges()

# loop this
changes['changelist'][opts[0].tag] = {
    'package-name': opts[0].package_name.replace(" ","-").replace("_","-"),
    'message': opts[0].message,
    'ref': opts[0].tag,
    'author-name': opts[0].author_name,
    'author-email': opts[0].author_email,
    'distributions': opts[0].distributions,
    'urgency': opts[0].urgency,
    'date': email.utils.format_datetime(datetime.datetime.fromtimestamp(parameters['commitdateraw'])),
}
load.write(changes)