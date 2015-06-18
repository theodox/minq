__author__ = 'stevet'
import maya.cmds as cmds

class Expression(object):

    def __init__(self, command, *args, **flags):
        self.command = command
        self.flags = flags
        self.args = args

    def _eval(self):
        result = self.command(*self.args, **self.flags)
        return result

    def eval(self):
        return tuple(self._eval() or tuple())



    def _format_expression(self, command, args, flags):
        cmd = command.__module__ + "." + command.__name__
        arglist = []
        if len(args):
            arglist.append("\n\t*" + args.__repr__())
        if len(flags):
            arglist.append("\n\t**" + flags.__repr__()) 
        return "{}({})".format(cmd, ",".join(arglist))

    def __iter__(self):
        return  iter(self._eval() or tuple())

    def __repr__(self):
        return self._format_expression(self.command, self.args, self.flags)

    def __call__(self, *args, **flags):
        self.args = args
        self.flags = flags


class ChainedExpression(Expression):

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



class DisjointExpression(Expression):

    def __init__(self, expr1, expr2):
        self.upstream = expr1
        self.downstream = expr2

    def _eval(self):
        return self.downstream.command(*self.upstream.eval(), **self.self.downstream.flags)
        
    def __repr__(self):
        flags = self.downstream.flags
        cmd = self.downstream.command
        return self._format_expression(cmd, tuple([self.upstream]), flags)

    def __call__(self, *args, **kwargs):
        self.downstream(*args, **kwargs)


class ChainableBase(Expression):
    CMD = cmds.ls
    FLAGS = {}

    def __init__(self, *args, **flags):
        flags.update(self.FLAGS)
        super(LSCommand, self).__init__(self.CMD, *args, **flags)

    @classmethod
    def can_chain(cls, other_cls):
        return cls.CMD == other_cls.CMD

    def compose(self, other_cls):
        downstream = other_cls()

        if self.can_chain(other_cls):
            return ChainedExpression(self, downstream)
        else:
            return DisjointExpression(self, downstream)


class LSCommand(ChainableBase):
    CMD = cmds.ls
    FLAGS = {'long': True}


class ListHistoryCommand(ChainableBase):
    CMD = cmds.listHistory

class ListRelativesCommand(ChainableBase):
    CMD = cmds.listRelatives
    FLAGS = {'fullPath': True}

class FindTypeCommand(ChainableBase):
    CMD = cmds.findType
    FLAGS = {'deep': True}