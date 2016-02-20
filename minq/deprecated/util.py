import itertools
from collections import namedtuple
XYZ = namedtuple('XYZ', 'x y z')


def get(expr):
    return expr.eval()


def first(expr):
    """
    return only the first item in the query, or None
    """
    return next((i for i in expr))


def last(expr):
    """
    return only the last item in the query, or None
    """
    final = None
    for item in expr:
        final = item
    return final


def parallel(*exprs):
    """
    return a zip of multiple queries. No guarantees are made about the ordering
    """
    return itertools.izip_longest(*exprs)