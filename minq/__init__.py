
"""
minq:  a query language for maya.

TLDR: You are free to use this as you like, provided you preserve the copyright
information. This copryight covers all of the modules in the minq project

Copyright (c) 2016 Steve Theodore

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


# core minq classes
from .core import *

# query proxy
from .item import item

# stream transformations
from .project import *

# NodeTypes like 'Meshes'
from .nodes import *

def using(*objects):
    """
    A convenience wrapper for starting a quuery with objects you alreadh know

    You can achieve the same thing with any stream class, but Streams expect an
    iterable input so you have to add extre brackets. This just makes that
    unnecessary.  Note that this will use the Scene() node to filter the objects,
    so that typos or other mistake will result in an empty stream.
    """
    return Scene(objects)