# Installation

```
sudo apt-add-repository 'deb http://ppa.launchpad.net/patchshorts/gutils/ubuntu focal main'
apt-get install deb-changectl
```

# How it works

deb-changectl only reads from the git log and writes to the changelog. It does this in a sensible way for the devops engineer to enable developers to have snapshot packages and release packages with a sensible versioning scheme.

# Help
```
Usage: deb-changectl [args] path/to/debian/changelog

Options:
  -h, --help            show this help message and exit
  -b BUILDNUM, --build-number=BUILDNUM
                        Specify the build number. This is factored into the
                        versions of snapshots.
  -p PACKAGE_NAME, --package-name=PACKAGE_NAME
                        Specify the package name writen to the changelog
  -m MESSAGE, --message=MESSAGE
                        Specify the change itself. i.e. Released tag 1.0.0
  -t TAG, --tag=TAG     If snapshot, specify the short commit hash, otherwise
                        use a tag(version)
  -c COMMIT, --commit=COMMIT
                        Specify the short commit hash that triggers the build.
                        Usually an environment variable in your cicd tool.
                        i.e. gitlab: $CI_COMMIT_SHORT_SHA
  -a AUTHOR_NAME, --author-name=AUTHOR_NAME
                        Specify the author of the change.
  -e AUTHOR_EMAIL, --author-email=AUTHOR_EMAIL
                        Specify the author's email.
  -d DISTRIBUTIONS, --distributions=DISTRIBUTIONS
                        Comma separated list of distros (i.e. bionic, sid,
                        buster, stable, unstable
  -u URGENCY, --urgency=URGENCY
                        Specify the package name writen to the changelog
  -R, --release         By default we assume snapshot mode, specify this to
                        issue release mode.
```
# Snapshot Example
Run inside any folder within a repo:

`deb-changectl -b 556 debian/changelog`

Output:

```
deb-changectl (0.0.3+554+86a8d290) stable; urgency=low


 testing package in action



 -- Chris Godwin <patchshorts@gmail.com>  Fri, 24 Apr 2020 04:49:06 -0000
 ```

# Release Example
For a release(tags only):
`deb-changectl -b 556 -R debian/changelog`
Output:
```
deb-changectl (0.0.3) stable; urgency=low

changed debian dependencies


 -- Chris Godwin <patchshorts@gmail.com>  Thu, 23 Apr 2020 03:52:42 -0000
 ```
# Gitlab CI/CD Example
`deb-changectl -b "${CI_JOB_ID}" -c "${CI_COMMIT_SHORT_SHA}" -t "${CI_COMMIT_SHORT_SHA}" -m "${CI_COMMIT_MESSAGE}" debian/changelog`
