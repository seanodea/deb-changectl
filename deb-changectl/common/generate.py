import sys
import debian

class generate(object):
    def itis(option):
        if option:
            return True
        else:
            return False
    def generate(self, option, changes):
        itis = self.itis(option)
        if itis:
            # put changes into changelog
            from debian.changelog import Changelog, Version
            changelog = Changelog()

            for change in changes['changelist']:
                data = changes['changelist'][change]

                changelog.new_block(package=data['package-name'],
                    version=data['ref'],
                    distributions=data['distributions'],
                    urgency=data['urgency'],
                    author=data['author-name'] + " <" + data['author-email'] + ">",
                    date=data['date'],
                )
                changelog.add_change('')
                changelog.add_change("     *  " + data['message'])
                changelog.add_change('')
                f = open(option, 'w')
                try:
                    changelog.write_to_open_file(f)
                finally:
                    f.close()
            sys.exit(0)
        else:
            pass