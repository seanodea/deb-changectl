#How it works

deb-changectl only manipulates its yaml configuration file. deb-genchange then creates or recreates debian/changelog from the yaml. This suite is designed to be run by gilab cicd, Jenkins or some other cicd toolset.

#Examples

deb-changectl add [ARGS]

deb-changectl remove [ARGS]

deb-changectl raise [ARGS]

deb-changectl raise -S SNAPSHOT [ARGS]

deb-changectl raise -R RELEASE [ARGS]

deb-changectl raise -R RELEASE --auto=git

this file is a place holder.