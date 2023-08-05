# this contains imports plugins that configure py.test for astropy tests.
# by importing them here in conftest.py they are discoverable by py.test
# no matter how it is invoked within the source tree.

from astropy.tests.pytest_plugins import *
from astropy.tests.pytest_plugins import pytest_addoption as astropy_pytest_addoption

# Uncomment the following line to treat all DeprecationWarnings as
# exceptions
enable_deprecations_as_exceptions()

import os
from astropy.tests.helper import pytest

# Uncomment and customize the following lines to add/remove entries
# from the list of packages for which version numbers are displayed
# when running the tests
try:
    PYTEST_HEADER_MODULES['Astropy'] = 'astropy'
except (NameError, KeyError):  # needed to support Astropy < 1.0
    pass

# This is to figure out the affiliated package version, rather than
# using Astropy's
try:
    from .version import version
except ImportError:
    version = 'dev'

try:
    packagename = os.path.basename(os.path.dirname(__file__))
    TESTED_VERSIONS[packagename] = version
except NameError:   # Needed to support Astropy <= 1.0.0
    pass
