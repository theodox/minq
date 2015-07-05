"""
This module collects all of the operators defined in the different submodules for convenience.

Typical usage:

    from minq.minq import *
    scene().assemblies().where(lambda r: 'root' in r)

"""

from .ls import *
from .projections import *
from .relations import *
from .item import item
from .filters import *
