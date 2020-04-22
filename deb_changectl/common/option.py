import optparse
import os
import sys
from vcsgit.commit import commit

class options():

    options = {}

    def getparameters(self):
        (repo, dir, projdir) = commit.getdir()
        parameters = commit.getrecentcommitdata(repo, dir)
        alltags = commit.getalltags(repo, dir)
        return (parameters, alltags)
    
    def parseoptions(self, args, parameters):
        parser = optparse.OptionParser(usage="deb_changectl [args]")
        parser.add_option("-p","--package-name", dest="package_name", default=parameters['package-name'], help="Specify the package name writen to the changelog")
        parser.add_option("-m","--message", dest="message", default=parameters['message'], help="Specify the change itself. i.e. Released tag 1.0.0")
        parser.add_option("-t","--tag", dest="tag", default=parameters['commithash'], help="If snapshot, specify the short commit hash, otherwise use a tag(version)")
        parser.add_option("-a","--author-name", dest="author_name", default=parameters['author'], help="Specify the author of the change.")
        parser.add_option("-e","--author-email", dest="author_email", default=parameters['email'], help="Specify the author's email.")
        parser.add_option("-d","--distributions", dest="distributions", default="stable", help="Comma separated list of distros (i.e. bionic, sid, buster, stable, unstable")
        parser.add_option("-u","--urgency", dest="urgency", default="low", help="Specify the package name writen to the changelog")
        parser.add_option("-R","--release", action="store_true", dest="release", default=False, help="By default we assume snapshot mode, specify this to issue release mode.")
        parser.add_option("-G","--generate", dest="generate", default=False, help="When this flag is given the path to a changelog is given behind it. All other tags except -R are ignored and changes.yaml is writen to /path/to/debian/changelog")
        options = parser.parse_args(args)

        try:
            if options[0].help:
                sys.exit(0)
        except:
            pass

        return options

class getopts():
  def get(self):
    optsobj = options()
    (parameters, alltags) = optsobj.getparameters()
    opts = optsobj.parseoptions(sys.argv, parameters)
    return opts, alltags, parameters