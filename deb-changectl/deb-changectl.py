#!/usr/bin/env python3
import sys
from option.main import Option
from vcsgit.main import Git
from release.main import Release
from snapshot.main import Snapshot

Opts = Option()
Git = Git(Opts.options)
#options = opts.parseoptions(sys.argv)

if Opts.options[0].release:
    # Release get all the tags, write them to changelog, exit
    Release = Release(Opts.options, Git.alltags)
else:
    # Snapshot: get all the tags, write them to changelog...
    # then get the latest commit, write it as a snapshot.
    Snapshot = Snapshot(Opts.options, Git)na