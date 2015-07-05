import itertools

__author__ = 'stevet'


from collections import namedtuple
XYZ = namedtuple('XYZ', 'x y z')


def get(expr):
    return expr.eval()


def parallel(*exprs):
    return itertools.izip_longest(*exprs)