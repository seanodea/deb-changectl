import sys
import debian

class Release:
    def __init__(self, opts, alltags):
        self.generate(opts, alltags)
    def generate(self, opts, changes):
            from debian.changelog import Changelog, Version
            changelog = Changelog()

            for change in changes:
                data = change

                changelog.new_block(package=data['package-name'],
                    version=data['ref'],
                    distributions=data['distributions'],
                    urgency=data['urgency'],
                    author=data['author-name'] + " <" + data['author-email'] + ">",
                    date=data['date'],
                )
                changelog.add_change('')
                changelog.add_change('  *' + data['message'])
                changelog.add_change('')
                f = open(opts[1][1], 'w')
                try:
                    changelog.write_to_open_file(f)
                    print("wrote to file: " + opts[1][1])
                finally:
                    f.close()
            sys.exit(0)
