"""
This submodule defines operators which filter the incoming results and return a subset of the incoming data
"""

import itertools
import re

from .core import Iterate
from projections import attribs
import maya.cmds as cmds


class where(Iterate):
    """
    Pass only items which pass the supplied predicate function.  For example:

        has_an_x = lambda p: x in p
        Scene('a', 'b', 'x').where(has_an_x)

    will return just 'x'
    """

    def _run(self, *args, **kwargs):
        return itertools.ifilter(self.expression, args)


class where_not(Iterate):
    """
    Pass only items which _fail_ the supplied predicate: the inverse of 'where'
    """

    def _run(self, *args, **kwargs):
        return itertools.ifilterfalse(self.expression, args)


class like(Iterate):
    """
    Pass only items whose short name is matched by the supplied regex.  So:

        Scene('top', 'bottom').like('to')

    will pass ('top', 'bottom'), while:

        Scene('top', 'bottom').like('^to')

    will only pass 'top' since the regex matches only the start of the string due to the '^'.

    You can also use the regex compile arguments:

        .like("xyz", re.I)

    will match ("XYZ", 'xyz' and 'XyZ')
    """

    def __init__(self, *args, **kwargs):
        super(like, self).__init__(*args, **kwargs)
        self.re = re.compile(".")

    def _run(self, *args, **kwargs):
        is_match = lambda p: self.re.search(p.rpartition("|")[-1]) is not None

        return itertools.ifilter(is_match, args)

    def __call__(self, *args):
        self.re = re.compile(*args)


class unlike(like):
    """
    The inverse of `like` : return items which DONT match the supplied regex
    """

    def _run(self, *args, **kwargs):
        is_match = lambda p: self.re.search(p.rpartition("|")[-1]) is not None

        return itertools.ifilterfalse(is_match, args)


class distinct(Iterate):
    """
    Returns only one copy of all incoming items. Useful for queries which return duplicate items.
    """

    def _run(self, *args, **kwargs):
        return iter(set(args))


class with_attrib(attribs):
    """
    A return only objects from the incoming stream which have 'attrib' :

        tuple(nodes().with_attrib('orthographic'))
        # Result: (u'|top|topShape', u'|side|sideShape', u'|persp|perspShape', u'|front|frontShape') #

    """

    def _run(self, *args, **kwargs):
        results = super(with_attrib, self)._run(*args, **kwargs)
        if not results:
            return tuple()
        objects = cmds.ls(*results, long=True, o=True) or []
        return iter(set(objects))
