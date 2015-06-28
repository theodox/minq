def extension(self, name):
    target_class = ExpressionMeta.get_type(name)
    if target_class is False:
        raise NameError, "No Expression named " + name
    return self.compose(target_class)


def command_proxy(*args, **kwargs):
    """
    a passthrough placeholder
    """
    return args


class ExpressionMeta(type):
    """
    Mark derived classes as expressions so they can be chained
    """
    _CLASSES = {}

    def __new__(cls, name, bases, dct):
        dct['__getattr__'] = extension
        dct['SOURCE_ONLY'] = dct.get('SOURCE_ONLY', False)
        ExpressionMeta._CLASSES[name] = type.__new__(cls, name, bases, dct)
        return ExpressionMeta._CLASSES[name]

    @staticmethod
    def get_type(name):
        return ExpressionMeta._CLASSES.get(name, False)


class Expression(object):
    """
    Base class representing a query operation. An individual expression represents a single transformation of one set
    of incoming data: for example, taking a selection list and finding upstream nodes
    """
    __metaclass__ = ExpressionMeta

    def __init__(self, *args, **flags):
        self.command = flags.get('command', command_proxy)
        if 'command' in flags:
            del flags['command']
        self.flags = flags
        self.args = args

    def _eval(self):
        result = self.command(*self.args, **self.flags)
        return result

    def eval(self):
        return tuple(self._eval() or tuple())

    def _format_expression(self, command, args, flags):
        cmd = command.__module__ + "." + command.__name__
        arg_list = []
        if len(args):
            arg_list.append("\n\t*" + args.__repr__())
        if len(flags):
            arg_list.append("\n\t**" + flags.__repr__())
        return "{}({})".format(cmd, ",".join(arg_list))


    def compose(self, other):
        assert not other.SOURCE_ONLY, "%s is a source node and can't be used downstream" % other
        return DisjointExpression(self, other())


    def __iter__(self):
        return iter(self._eval() or tuple())


    def __repr__(self):
        return self._format_expression(self.command, self.args, self.flags)


    def __call__(self, *args, **flags):
        self.args = args
        self.flags = flags


    def __add__(self, other):
        result = iter(set(self).union(set(other)))
        return Expression(*result)


    def __sub__(self, other):
        result = iter(set(self).difference(set(other)))
        return Expression(*result)


    def __xor__(self, other):
        result = iter(set(self).symmetric_difference(set(other)))
        return Expression(*result)


    def __and__(self, other):
        result = iter(set(self).intersection(set(other)))
        return Expression(*result)


    def __invert__(self):
        """
        use the tilde as shortcut for 'eval'
        """
        return self.eval()


class ChainedExpression(Expression):
    """
    Represents two similar expressions which can be collapsed: for example, two ls.py() commands which can be
    combined into a single call by combining flags
    """

    def __init__(self, expr1, expr2):
        self.upstream = expr1
        self.downstream = expr2

    def _concat(self):
        args = self.upstream.args + self.downstream.args
        flags = dict(self.upstream.flags)
        flags.update(self.downstream.flags)
        return args, flags

    def _eval(self):
        args, flags = self._concat()
        return self.downstream.command(*args, **flags)

    def __repr__(self):
        args, flags = self._concat()
        cmd = self.upstream.command
        return self._format_expression(cmd, args, flags)

    def __call__(self, *args, **kwargs):
        self.downstream(*args, **kwargs)
        return self


class DisjointExpression(Expression):
    """
    Represents pair of expressions which can't be chained. the "upstream" expression will be evaluated and the
    results passed to the downstream expression as arguments
    """

    def __init__(self, expr1, expr2):
        self.upstream = expr1
        self.downstream = expr2

    def _eval(self):
        return self.downstream.command(*self.upstream.eval(), **self.downstream.flags)

    def __repr__(self):
        flags = self.downstream.flags
        cmd = self.downstream.command
        return self._format_expression(cmd, tuple([self.upstream]), flags)

    def __call__(self, *args, **kwargs):
        self.downstream(*args, **kwargs)
        return self


class Operator(Expression):
    """
    Base class for simple maya commands: It's an expression that can be pointed at a command and a set of flags using
    class-level variables
    """
    CMD = command_proxy()
    FLAGS = {}

    def __init__(self, *args, **flags):
        d = dict(**flags)
        d.update(self.FLAGS)
        d['command'] = self.CMD
        super(Operator, self).__init__(*args, **d)

    @classmethod
    def can_chain(cls, other_cls):
        """
        override to provide special logic, eg for cmds.ls.py which has incompatible flags
        """
        return issubclass(other_cls, Operator) \
               and cls.CMD == other_cls.CMD

    def compose(self, other_cls):
        assert not other_cls.SOURCE_ONLY, "%s is a source node and can't be used downstream" % other_cls

        downstream = other_cls()

        if self.can_chain(other_cls):
            return ChainedExpression(self, downstream)
        else:
            return DisjointExpression(self, downstream)


class DisjointOperator(Expression):
    """
    An operator which can't be chained - the base class for any operation which always forces upstream operators to
    evaluate before proceeding
    """
    CMD = command_proxy
    FLAGS = {}

    def __init__(self, *args, **flags):
        d = dict(**flags)
        d.update(self.FLAGS)
        d['command'] = self.CMD
        super(DisjointOperator, self).__init__(*args, **d)

    def compose(self, other_cls):
        assert not other_cls.SOURCE_ONLY, "%s is a source node and can't be used downstream" % other_cls

        downstream = other_cls()
        return DisjointExpression(self, downstream)

