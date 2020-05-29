import sys
import debian

class Snapshot:
    def __init__(self, opts, git):
        self.generate(opts, git)
    def generate(self, opts, git):
            from debian.changelog import Changelog, Version
            changelog = Changelog()

            for change in git.alltags:
                data = change

                changelog.new_block(package=data['package-name'],
                    version=data['ref'],
                    distributions=data['distributions'],
                    urgency=data['urgency'],
                    author=data['author-name'] + " <" + data['author-email'] + ">",
                    date=data['date'],
                )
                changelog.add_change('')
                changelog.add_change('  * ' + data['message'])
                changelog.add_change('')
            f = open(opts[1][1], 'w')
            try:
                changelog.write_to_open_file(f)
            finally:
                f.close()
            changelog.new_block(package=git.headcommit['package-name'],
                version=git.latesttag[0]['ref'] + "+" + str(opts[0].buildnum) + '+' + str(git.headcommit['commithash']),
                distributions=git.headcommit['distributions'],
                urgency=git.headcommit['urgency'],
                author=git.headcommit['author-name'] + " <" + git.headcommit['author-email'] + ">",
                date=git.headcommit['date'],
            )
            changelog.add_change("\n")
            changelog.add_change('  * ' + git.headcommit['message'])
            changelog.add_change("\n")
            
            f = open(opts[1][1], 'w')
            try:
                changelog.write_to_open_file(f)
                print("wrote to file: " + opts[1][1])
            finally:
                f.close()
            sys.exit(0)
