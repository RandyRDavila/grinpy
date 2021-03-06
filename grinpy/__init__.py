# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>

# check Python version
# TODO: determine actual minimum version required. Here, the development version is used.
import sys
if sys.version_info[:2] < (3, 6):
    m = "Python 3.6 or later is required for GrinPy (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

# import NetworkX dependency
import networkx
from networkx import *

# the following are imported orderwise
import grinpy.classes
from grinpy.classes import *

import grinpy.functions
from grinpy.functions import *

import grinpy.invariants
from grinpy.invariants import *
