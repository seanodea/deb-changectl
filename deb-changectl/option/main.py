import sys, optparse

class Option:

    options = object

    def __init__(self):
        self.options = self.parseoptions(sys.argv)
    
    def parseoptions(self, args):
        parser = optparse.OptionParser(usage="deb-changectl [args]")
        parser.add_option("-b", "--build-number", dest="buildnum", default=False, help="Specify the build number. This is factored into the versions of snapshots.")
        parser.add_option("-p","--package-name", dest="package_name", default="", help="Specify the package name writen to the changelog")
        parser.add_option("-m","--message", dest="message", default="", help="Specify the change itself. i.e. Released tag 1.0.0")
        parser.add_option("-t","--tag", dest="tag", default="", help="If snapshot, specify the short commit hash, otherwise use a tag(version)")
        parser.add_option("-c","--commit", dest="commit", default="", help="Specify the short commit hash that triggers the build. Usually an environment variable in your cicd tool. i.e. gitlab: $CI_COMMIT_SHORT_SHA")
        parser.add_option("-a","--author-name", dest="author_name", default="", help="Specify the author of the change.")
        parser.add_option("-e","--author-email", dest="author_email", default="", help="Specify the author's email.")
        parser.add_option("-d","--distributions", dest="distributions", default="stable", help="Comma separated list of distros (i.e. bionic, sid, buster, stable, unstable")
        parser.add_option("-u","--urgency", dest="urgency", default="low", help="Specify the package name writen to the changelog")
        parser.add_option("-R","--release", action="store_true", dest="release", default=False, help="By default we assume snapshot mode, specify this to issue release mode.")
        options = parser.parse_args(args)

        # Process help
        try:
            if options[0].help:
                sys.exit(0)
        except:
            pass

        # Sanity check
        if not options[0].buildnum:
            print("The build number is required. See -h for help.")
            sys.exit(0)
        return options