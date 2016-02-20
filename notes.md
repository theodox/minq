

sample queries



nodes.meshes.where(item.parent.tx > 5)
nodes.lights.where(item.intensity > 5)
transforms.where(item.child is mesh)
selected.meshes
selected.transforms
joints.below('joint1')
joints.above('joint5')
selected.children.meshes


basic concepts:

- query: get a set of things
    - records: sets are basically tables and can have 'columns'.  All queries have at least one.
    - implicit sets: for maya objects, everything has implictly got transform properties
    
    
- filter: 
    - subsets a record set based on some predicate
    
- set operations:
    - new set which is a union, difference or intersection of other sets

- joins:
    - new set which creates extra fields in on set using data in another
    


example = query(objects, positions).where(position.x > 10)


====
sample code


def Type(p):
    return cmds.nodeType(p)
    
def Selected(p):
    return len(cmds.ls(p, sl=True)) == 1   
        
class Position(object):
    
    @staticmethod
    def local(p):
        return tuple(cmds.xform(p,t=True, q=True))
    
    @staticmethod
    def world(p):
        return tuple(cmds.xform(p,t=True, q=True, ws=True))
    

class Query(object):
    def __init__(self, *fields):
        self.fields = fields
        
    def eval(self):
        nodes = cmds.ls(dag=True, l=True)
        for node in nodes:
            try:
                yield (node, tuple((f(node) for f in self.fields)))
            except RuntimeError:
                pass            

    def join(self, other):
        my_results = dict(self.eval())
        their_results = dict(other.eval())
        for k, v in my_results.items():
            if k in their_results:
                yield k, v + their_results[k]
    
    def where(self, predicate):
        for obj, columns in self.eval():
            if predicate(columns[0]):
                yield obj, columns

    

lcl = Query(Position.local)
ty = Query(Selected)
wr = Query(Position.world)
for item in lcl.where(lambda p: p[1] == 0):
    print item
    
    
    
#--------------

'result first' query

meshes.where(xxx == yyy).under(xxxx)
meshes.where(polycount > 50).like('small')
curves.connected_to(ddd)

transforms.where(tx > .5) >> tx

joints.where(joint.below('some_joint'))
joints.where(joint.contains('finger_01') & joint.like('hand')) >> transforms()



#---- two basic ops: filter ('only') and transform ('get')

Joints().where(item.tx > 5).get(Children).only(Meshes).like('xx')



#----
from maya.api.OpenMaya import *
cmds.objectType('pCubeShape1', tt=True)

mm = MNodeClass('mesh')
mm.typeId

dir (MFnCamera)

dir(MFn)
dir(mm)
dir(MFnCamera)




def iter_type(ktype):
    
    sel = MGlobal.getSelectionListByName('*')
    ss = MItSelectionList(sel, ktype)
    #md = MFnDependencyNode()
    while not ss.isDone():
        yield MFnDependencyNode(ss.getDependNode())
        
        
for item in iter_type(MFn.kCamera):
    print item, item.name   
    
#cmds.ls()





