import os
import sys
import datetime
import git
from pathlib import Path
import email.utils
from conf import confyaml

class commit():
    
    def getdir():
      dir = os.getcwd()
      try:
        repo = git.Repo(dir)
      except git.exc.InvalidGitRepositoryError:
        try:
          repo = git.Repo(Path(dir).parent)
          dir = Path(dir).parent
        except git.exc.InvalidGitRepositoryError:
          try:
            repo = self.getgit(Path(dir).parent)
            dir = Path(dir).parent
          except:
            print("Something went wrong. Valid repo? Permissions?")
            sys.exit(1)
      return (repo, os.path.basename(os.path.normpath(dir)), os.path.normpath(dir))

    def releaseortag(opts, alltags, parameters):
      # options processing
      if opts[0].release == True:
        return alltags
      else:
        # Getting yaml file contents
        latesttagkey = next(iter(alltags['changelist']))
        latesttag = alltags['changelist'][latesttagkey]
        load = confyaml.load()
        changes = load.getchanges(commit.getdir()[2])
        changes['changelist'][opts[0].tag] = {
            'package-name': opts[0].package_name.replace(" ","-").replace("_","-"),
            'message': opts[0].message,
            'ref': latesttag['ref'] + '_' + opts[0].tag,
            'author-name': opts[0].author_name,
            'author-email': opts[0].author_email,
            'distributions': opts[0].distributions,
            'urgency': opts[0].urgency,
            'date': email.utils.format_datetime(datetime.datetime.fromtimestamp(parameters['commitdateraw'])),
        }
        return changes

    def getrecentcommitdata(repo, pdir):

        try:
          head = repo.head.reference
        except TypeError:
          head = repo.head
          print("Detached head detected, compensating...Done.")

        commitdata = {
          'package-name': pdir,
          'branch': head.name,
          'commithash': head.commit.hexsha[0:8],
          'message': head.commit.message,
          'commitdateraw': head.commit.committed_date,
          'author': head.commit.author.name,
          'email': head.commit.author.email,
        }
        return commitdata

    def getalltags(repo, dir):
      changes = {'changelist': {}}
      tags = repo.tags
      # foreach tag as .
      for tag in tags:
        tagref = tag
        commit = tagref.commit
        changes['changelist'][commit.hexsha[0:8]] = {
          'package-name': dir.replace(" ","-").replace("_","-"),
          'message': commit.message,
          'ref': tagref.name,
          'author-name': commit.author.name,
          'author-email': commit.author.email,
          'distributions': 'oldstable,stable,unstable',
          'urgency': 'medium',
          'date': email.utils.format_datetime(datetime.datetime.fromtimestamp(commit.committed_date)),
        }
        return changes