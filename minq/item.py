__author__ = 'stevet'
import operator

import maya.cmds as cmds
from collections import namedtuple

XYZ = namedtuple ('XYZ', 'x y z')

class AttributeQuery(object):

    # these attribs are return as tuples-in-lists by getAttr, so we unpack them
    UNPACK_MULT = ('t', 'translate', 'r', 'rotate', 's', 'scale', 'rp', 'rotatePivot', 'sp', 'scalePivot')

    def __init__(self, attribName, operator=None, comp=None, strict=False):
        self.attrib = attribName
        if self.attrib[0] == ".":
            self.attrib = attribName[1:]
        self.comp = comp
        self.operator = operator
        self.strict = strict
        self.unpack = self.attrib in self.UNPACK_MULT

    def __repr__(self):
        lookup = {
            operator.eq: "==",
            operator.ge: ">=",
            operator.gt: ">",
            operator.le: "<=",
            operator.lt: "<",
            operator.ne: "!=",
            operator.rshift: None,
            None: '?'
        }
        if lookup.get(self.operator):
            return "{attribute: %s %s %s}" % (self.attrib, lookup[self.operator], self.comp)
        else:
            return "%s({attribute: %s})" % (str(self.comp), self.attrib)

    def eval(self, maya_obj):
        try:
            value = cmds.getAttr("{}.{}".format(maya_obj, self.attrib))
            if self.unpack:
                value = XYZ(*value[0])
            if self.operator != operator.rshift:
                return self.operator(value, self.comp)
            else:
                return self.comp(value)
        except:
            if self.strict:
                raise
            return False

    def __eq__(self, other):
        return AttributeQuery(self.attrib, operator=operator.eq, comp=other)

    def __ne__(self, other):
        return AttributeQuery(self.attrib, operator=operator.ne, comp=other)

    def __gt__(self, other):
        return AttributeQuery(self.attrib, operator=operator.gt, comp=other)

    def __ge__(self, other):
        return AttributeQuery(self.attrib, operator=operator.ge, comp=other)

    def __lt__(self, other):
        return AttributeQuery(self.attrib, operator=operator.lt, comp=other)

    def __le__(self, other):
        return AttributeQuery(self.attrib, operator=operator.le, comp=other)

    def __rshift__(self, other):
        return AttributeQuery(self.attrib, operator=operator.rshift, comp=other)

    def __call__(self, maya_obj):
        return self.eval(maya_obj)


def attribute_factory(*args, **kwargs):
    return AttributeQuery(args[1])


class ItemMeta(type):
    def __new__(cls, name, bases, dct):
        result = type.__new__(cls, name, bases, dct)
        setattr(result.__class__, '__getattr__', attribute_factory)
        return result


class item(object):
    """
    Proxies for attribute queries against maya objects
    """
    __metaclass__ = ItemMeta
