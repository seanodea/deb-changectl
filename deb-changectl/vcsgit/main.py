import os, sys, datetime, git, email.utils
from pathlib import Path

class Git:

    repo = object
    repocwd = ""
    repodir = ""
    alltags = []
    latesttag = []
    headcommit = {}


    def __init__(self, opts):
        # Get the repo and repodir
        # 
        (self.repo,self.repodir,self.repocwd) = self.getrepodir()
        self.gettags(opts[0])
        self.getheadcommit(opts[0])
     
    def getrepodir(self):
        directory = os.getcwd()
        try:
            repo = git.Repo(directory)
        except git.exc.InvalidGitRepositoryError:
            try:
                repo = git.Repo(Path(directory).parent)
                directory = Path(directory).parent
            except:
                try:
                    repo = self.getgit(Path(directory).parent)
                    directory = Path(directory).parent
                except:
                    print("Reached rootfs. Valid repo? Permissions?")
                    sys.exit(1)
        return (repo, os.path.basename(os.path.normpath(directory)), os.path.normpath(directory))
    def gettags(self, opts):
        utags = self.repo.tags
        tags = sorted(utags, key=lambda t: t.commit.committed_datetime)
        # foreach tag as .
        i = len(tags)
        for tag in tags:
            self.alltags.append({
                'package-name': self.repodir.replace(" ","-").replace("_","-"),
                'message': tag.commit.message,
                'ref': tag.name,
                'author-name': tag.commit.author.name,
                'author-email': tag.commit.author.email,
                'urgency': opts.urgency,
                'date': email.utils.format_datetime(datetime.datetime.fromtimestamp(tag.commit.committed_date)),
                'distributions': opts.distributions,
            })
            i -= 1
        try:
            self.latesttag = self.alltags[len(self.alltags)-1]
        except:
            self.latesttag.append({'ref': "0.0.0"})
    def getheadcommit(self, opts):
        try:
            head = self.repo.head.reference
        except TypeError:
            head = self.repo.head
            print("Detached head detected, compensating...Done.")

        try:
            self.headcommit = {
                'package-name': self.repodir.replace(" ","-").replace("_","-"),
                'branch': head.name,
                'commithash': head.commit.hexsha[0:8],
                'message': head.commit.message,
                'date': email.utils.format_datetime(datetime.datetime.fromtimestamp(head.commit.committed_date)),
                'dateraw': head.commit.committed_date,
                'author-name': head.commit.author.name,
                'author-email': head.commit.author.email,
                'urgency': opts.urgency,
                'distributions': opts.distributions,
            }
        except ValueError:
            print("Cannot find any commits. Is this an new repo?")
            sys.exit(2)
