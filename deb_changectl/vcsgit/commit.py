import os
import datetime
import git
from pathlib import Path

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