__author__ = 'stevet'
import operator

import maya.cmds as cmds

from collections import namedtuple

XYZ = namedtuple('xyz', 'x y z')

from minq.core import Where, WhereMany, Stream


class AttributeQuery(object):
    """
    This is a query-generation helper class.  You can use it to create (simple) attribute value tests inside a query
    like `where` that takes a callable predicate.  For example:

        Cameras().where(item.orthographic == True))

    will find all the scene camera with their 'orthographic' attribute set True, while

        meshes().parents.where(item.ty > 0)

    will find all mesh parent transforms whose translate Y attribute is larger than zero.

    strict
    ------

    By defaut, an AttributeQuery will ignore any objects which don't have the attribute you're checking.
    An item that doesn't have the attribute will fail the test: so, if a shape is mixed in with a collection of
    transforms, for example, it will fail both item.ty > 0 and item.ty < 0 since it has no 'ty' attribute.

    You can use a stricter evaluation to identify queries that produce bad attribute checks.  If you create the item
    separately and set it's "strict" property to true, it will except when it can't find the attribute:

        is_ortho = item.orthographic == True
        is_ortho.strict = True

        meshes().where(is_ortho)

    will raise a RuntimeException or ValueException when evaluated, since meshes don't have an `orthographic` attribute.


    unpack
    -------

    If the attribute you're testing is compound with XYZ values (such as translate, rotate or scale), the query will
    automatically work around Maya's annoying default behavior of returning these values as nested lists:

        cmds.getAttr('pCube1.t')
        # Result: [(0,0,0)]

    an item query will instead see the result as (0,0,0), which means you can write:

        some_query.where(item.t == (0,0,0) )

    position, rotation, scale and pivot attributes will be automatically unpacked for you. If you want to unpack
    another attribute, set the unpack flag on your query:

        q = item.displayColor == (1,0,0)
        q.unpack = True


    query_type
    ----------

    The query object includes a field called `query_type`, which tells a stream whether to use a fast bulk query (the
    minq.core.WhereMany class) or a slower but more flexible query the (minq.core.Where). WhereMany is preferable for
    built-in attributes, but -- thanks to a Maya limitation -- it does not work with custom attributes.  When in doubt,
    setting query_type to `Where` will always work, although it won't be as speedy.

    The `native' proxy class always uses `WhereMany`.  The `custom` proxy always uses `Where`.
    """
    # these attribs are return as tuples-in-lists by getAttr, so we unpack them
    UNPACK_MULT = ('t', 'translate', 'r', 'rotate', 's', 'scale', 'rp', 'rotatePivot', 'sp', 'scalePivot')
    QUERY_CLASS = Where

    def __init__(self, attribute, operator=None, comp=None):
        self.attribute = attribute
        if self.attribute[0] == ".":
            self.attribute = attribute[1:]
        self.comp = comp
        self.operator = operator
        self.unpack = self.attribute in self.UNPACK_MULT
        self.query_type = self.QUERY_CLASS
        self.strict = False

    def __repr__(self):
        lookup = {
            operator.eq: "==",
            operator.ge: ">=",
            operator.gt: ">",
            operator.le: "<=",
            operator.lt: "<",
            operator.ne: "!="
        }
        if lookup.get(self.operator):
            return "{attribute: %s %s %s}" % (self.attribute, lookup[self.operator], self.comp)
        else:
            return "%s({attribute: %s})" % (str(self.comp), self.attribute)

    def eval(self, obj):
        try:
            value = cmds.getAttr(obj + "." + self.attribute)
            if self.unpack:
                value = value[0]
            return self.operator(value, self.comp)
        except RuntimeError:
            if self.strict:
                raise
            return False
        except ValueError:
            if self.strict:
                raise
            return False

    def __eq__(self, other):
        return self.__class__(self.attribute, operator=operator.eq, comp=other)

    def __ne__(self, other):
        return self.__class__(self.attribute, operator=operator.ne, comp=other)

    def __gt__(self, other):
        return self.__class__(self.attribute, operator=operator.gt, comp=other)

    def __ge__(self, other):
        return self.__class__(self.attribute, operator=operator.ge, comp=other)

    def __lt__(self, other):
        return self.__class__(self.attribute, operator=operator.lt, comp=other)

    def __le__(self, other):
        return self.__class__(self.attribute, operator=operator.le, comp=other)

    def __call__(self, value):
        return self.eval(value)


class NativeAttributeQuery(AttributeQuery):
    QUERY_CLASS = WhereMany


class ItemMeta(type):
    def __new__(cls, name, bases, dct):
        def attribute_factory(*args, **kwargs):
            result = AttributeQuery(args[1])
            return result

        result = type.__new__(cls, name, bases, dct)
        setattr(result.__class__, '__getattr__', attribute_factory)
        return result


class QueryExtension(object):
    """
    Base class for 'item' query factory classes. Any methods here must be class methods
    """
    @classmethod
    def has(cls, *args, **kwargs):
        """
        used for shorthand tests like  `item.has(Children)`
        """

        def anon(obj):
            return any(Stream((obj,)).get(*args, **kwargs))
        return anon

    @classmethod
    def has_attr(cls, attr):
        """
        used for shorthand tests like `item.has_attr("orthographic")`
        """
        def anon(obj):
            return any(cmds.ls(obj + "." + attr))
        return anon


class item(QueryExtension, metaclass=ItemMeta):
    """
    This stands in for attribute queries against maya objects.  When used in a stream, it generates an
    AttributeQuery in-line for you.

        Transforms().where(item.visible == True)

    is the same as

        Transforms().where(lambda p: cmds.getAttr(p, "visible") == True)

    Under the hood the call to `item` simple converts into an AttributeQuery object at evaluation time.

    A query created by `item` uses the `Where` path when used in a stream (see the note to AttributeQuery, above).
    It's better practice to explicity use `native` or `custom` in preference to item if you know that your
    attributes are or are not user-defined -- using `native` where you can will improve perf when you are working with
    built-in Maya attributes.
    """


class custom(QueryExtension, metaclass=ItemMeta):
    """
    custom is a synonym for `item`.  It's good practice to use `custom` when you know that an attribute is user-defined,
    since it will tell other users that they can't switch in `native` without generating exceptions.
    """


class NativeMeta(type):
    def __new__(cls, name, bases, dct):
        def custom_attribute_factory(*args, **kwargs):
            result = NativeAttributeQuery(args[1])
            return result

        result = type.__new__(cls, name, bases, dct)
        setattr(result.__class__, '__getattr__', custom_attribute_factory)
        return result


class native(QueryExtension, metaclass=NativeMeta):
    """
    Like `item`, this generates a proxy query. Queries from `native` only work for built-in Maya attributes -- if you
    run a native query against a user-defined attribute you'll get an exception.  However `native` queries will execute
    faster than the same query using `item` or `custom`.
    """
