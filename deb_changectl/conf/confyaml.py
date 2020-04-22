import sys, os
sys.path.insert(0, os.path.abspath('..'))

import yaml
from vcsgit import commit


class load():
    def getchanges(self, dir):
        try:
            with open(dir + "/changes.yaml", 'r') as yamlstream:
                # NoneType error is happening here
                changes = yaml.load(yamlstream,Loader=yaml.FullLoader)
        except PermissionError:
            print("You don't have permissions on changes.yaml or the git directory.")
            sys.exit(1)
        except:
            changes = {'changelist': {}}
        if changes == None:
            changes = {'changelist': {}}
        return changes
class write():
    def put(self, changes, dir):
        try:
            with open(dir + "/changes.yaml", 'w') as outfile:
                yaml.dump(changes, outfile, default_flow_style=False)
                print("wrote changes to " + dir + "/changes.yaml. Now run deb_changectl --generate /path/to/debian/changelog.")
        except PermissionError:
            print("You don't have permissions on changes.yaml or the git directory.")
            sys.exit(1)