#!/usr/bin/env python3

import sys
import email.utils
import os
import yaml
from common.option import options
from conf import confyaml
import datetime
# Parse options and fetch defaults from git
optsobj = options()
(parameters, alltags) = optsobj.getparameters()
opts = optsobj.parseoptions(sys.argv, parameters)

# options processing
if opts[0].release == True:
  confyaml.write(alltags)
else:
  # Getting yaml file contents
  changes = confyaml.load.getchanges()
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
  confyaml.write(changes)