import os
import datetime
import git
from pathlib import Path
import email.utils

class commit():
    
    def getdir(dir):
        try:
          repo = git.Repo(dir)
        except git.exc.InvalidGitRepositoryError:
          try:
            repo = git.Repo(Path(dir).parent)
          except git.exc.InvalidGitRepositoryError:
            repo = self.getgit(Path(dir).parent)
        return (repo, os.path.basename(os.path.normpath(dir)))
    def getrecentcommitdata(repo, dir):

        head = repo.head.reference

        commitdata = {
          'package-name': dir,
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