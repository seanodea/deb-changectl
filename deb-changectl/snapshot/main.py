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
                changelog.add_change(data['message'])
                changelog.add_change('')
            f = open(opts[1][1], 'w')
            try:
                changelog.write_to_open_file(f)
            finally:
                f.close()
            changelog.new_block(package=git.headcommit['package-name'],
                version=git.latesttag['ref'] + "+" + str(opts[0].buildnum) + '+' + str(git.headcommit['commithash']),
                distributions=git.headcommit['distributions'],
                urgency=git.headcommit['urgency'],
                author=git.headcommit['author-name'] + " <" + git.headcommit['author-email'] + ">",
                date=git.headcommit['date'],
            )
            changelog.add_change("\n")
            changelog.add_change(' ' + git.headcommit['message'])
            changelog.add_change("\n")
            
            print(repr(opts[1]))
            f = open(opts[1][1], 'w')
            try:
                changelog.write_to_open_file(f)
                print("wrote to file: " + opts[1][1])
            finally:
                f.close()
            sys.exit(0)

            '''            self.headcommit = {
                'package-name': self.repodir.replace(" ","-").replace("_","-"),
                'branch': head.name,
                'commithash': head.commit.hexsha[0:8],
                'message': head.commit.message,
                'date': email.utils.format_datetime(datetime.datetime.fromtimestamp(head.commit.committed_date)),
                'dateraw': head.commit.committed_date,
                'author': head.commit.author.name,
                'email': head.commit.author.email,
                'urgency': opts.urgency,
                'distributions': opts.distributions,
            }'''