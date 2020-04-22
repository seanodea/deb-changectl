#!/usr/bin/env python3

import sys, os, yaml, email.utils
from common.option import options
from common.option import getopts
from common.generate import generate
from conf import confyaml
from vcsgit.commit import commit
# Parse options and fetch defaults from git

(repo, basename, projdir) = commit.getdir()

getops = getopts()
(opts, alltags, parameters) = getopts.get(projdir)

changes = commit.releaseortag(opts, alltags, parameters)
generate = generate.generate(generate, opts[0].generate, changes)
confyaml.write().put(changes, projdir)