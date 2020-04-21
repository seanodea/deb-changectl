import optparse
import os
from vcsgit.commit import commit

class options():

    options = {}

    def getparameters(self):
        (repo, dir) = commit.getdir(os.getcwd())
        parameters = commit.getcommitdata(repo, dir)
        return parameters
    
    def parseoptions(self, args, parameters):
        parser = optparse.OptionParser(usage="run with -h for help.")
        parser.add_option("-p","--package-name", dest="package_name", default=parameters['package-name'], help="Specify the package name writen to the changelog")
        parser.add_option("-m","--message", dest="message", default=parameters['message'], help="Specify the change itself. i.e. Released tag 1.0.0")
        parser.add_option("-t","--tag", dest="tag", default=parameters['commithash'], help="If snapshot, specify the short commit hash, otherwise use a tag(version)")
        parser.add_option("-a","--author-name", dest="author_name", default=parameters['author'], help="Specify the author of the change.")
        parser.add_option("-e","--author-email", dest="author_email", default=parameters['email'], help="Specify the author's email.")
        parser.add_option("-d","--distributions", dest="distributions", default="stable", help="Comma separated list of distros (i.e. bionic, sid, buster, stable, unstable")
        parser.add_option("-u","--urgency", dest="urgency", default="low", help="Specify the package name writen to the changelog")
        options = parser.parse_args(args)

        try:
            if options[0].help:
                sys.exit(0)
        except:
            pass
        
        return options