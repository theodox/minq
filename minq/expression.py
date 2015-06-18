__author__ = 'stevet'


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

    def __repr__(self):
        return self._format_expression(self.command, self.args, self.flags)


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
        

class DisjointExpression(Expression):

    def __init__(self, expr1, expr2):
        self.upstream = expr1
        self.downstream = expr2

    def _eval(self):
        return self.downstream.command(*self.upstream.eval(), **self.flags)
        
    def __repr__(self):
        flags = self.downstream.flags
        cmd = self.downstream.command
        return self._format_expression(cmd, tuple([self.upstream]), flags)

Pretest = Expression(cmds.ls, l = True)
PrePreTest = Expression(cmds.ls, 'pCube1', 'top', 'pCubeShape1')
Test1 = ChainedExpression(Pretest, PrePreTest)
Test2 = Expression(cmds.listHistory, fl=True)
Test3 = Expression(cmds.listRelatives, p=True)
Test4 = Expression(cmds.ls, l=True)
x = DisjointExpression(Test1, Test2)
y = DisjointExpression(x, Test3)
z = DisjointExpression(y, Test4)
q = DisjointExpression(Test2, Expression(cmds.findType, type='polyCube'))
print q
print eval(str(q))
print maya.cmds.ls(
    *[maya.cmds.listRelatives(
        *[maya.cmds.listHistory(
            *[maya.cmds.ls(
                *('pCube1',),**{'l': True})],
            **{'fl': True})],
        **{'p': True})],
    **{'l': True})

print (i for i in (maya.cmds.ls(
	*[maya.cmds.listRelatives(
	    *[maya.cmds.listHistory(
	        *[maya.cmds.ls(
	            *('pCube1',),
	            **{'l': True})],
	        **{'fl': True})],
	    **{'p': True})],
	**{'l': True})))