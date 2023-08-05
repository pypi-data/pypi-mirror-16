"""
XStatic resource package

See package 'XStatic' for documentation and basic tools.
"""

DISPLAY_NAME = 'Angular-Bootstrap' # official name, upper/lowercase allowed, no spaces
PACKAGE_NAME = 'XStatic-%s' % DISPLAY_NAME # name used for PyPi

NAME = __name__.split('.')[-1] # package name (e.g. 'foo' or 'foo_bar')
                               # please use a all-lowercase valid python
                               # package name

VERSION = '0.11.0' # version of the packaged files, please use the upstream
                  # version number
BUILD = '8' # our package build number, so we can release new builds
             # with fixes for xstatic stuff.
PACKAGE_VERSION = VERSION + '.' + BUILD # version used for PyPi

DESCRIPTION = "%s %s (XStatic packaging standard)" % (DISPLAY_NAME, VERSION)

PLATFORMS = 'any'
CLASSIFIERS = []
KEYWORDS = '%s xstatic' % NAME

# XStatic-* package maintainer:
MAINTAINER = 'Maxime Vidori'
MAINTAINER_EMAIL = 'maxime.vidori@enovance.com'

# this refers to the project homepage of the stuff we packaged:
HOMEPAGE = 'http://angular-ui.github.io/bootstrap/'

# this refers to all files:
LICENSE = '(same as Angular-Bootstrap)'

from os.path import join, dirname
BASE_DIR = join(dirname(__file__), 'data')
# linux package maintainers just can point to their file locations like this:
#BASE_DIR = '/usr/share/javascript/angular_cookies'

LOCATIONS = {
    # CDN locations (if no public CDN exists, use an empty dict)
    # if value is a string, it is a base location, just append relative
    # path/filename. if value is a dict, do another lookup using the
    # relative path/filename you want.
    # your relative path/filenames should usually be without version
    # information, because either the base dir/url is exactly for this
    # version or the mapping will care for accessing this version.
}
