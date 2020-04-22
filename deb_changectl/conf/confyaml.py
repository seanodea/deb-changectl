import yaml

class load():
    def getchanges():
        try:
            with open("changes.yaml", 'r') as yamlstream:
                # NoneType error is happening here
                changes = yaml.load(yamlstream,Loader=yaml.FullLoader)
        except:
            changes = {'changelist': {}}
        if changes == None:
            changes = {'changelist': {}}
        print(repr(changes))
        return changes
class write(object):
    def __init__(self, changes):
        with open("changes.yaml", 'w') as outfile:
            yaml.dump(changes, outfile, default_flow_style=False)