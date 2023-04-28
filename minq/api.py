# core minq classes
from . import core

# query proxy
from .item_query import item, custom, native

# stream transformations
from .project import *

# NodeTypes like 'Meshes'
from .nodes import *

def using(*objects):
    """
    A convenience wrapper for starting a query with objects you alreadh know

    You can achieve the same thing with any stream class, but Streams expect an
    iterable input so you have to add extre brackets. This just makes that
    unnecessary.  Note that this will use the Scene() node to filter the objects,
    so that typos or other mistake will result in an empty stream.
    """
    return Scene(objects)