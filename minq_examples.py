'''
this file provides a few examples of minq idioms
make sure the minq module is on the your path and execute this inside a maya 
scene (ideally, one with a few kinds of objects
'''

from minq import *

# a few examples of  basic minq concepts

# all mesh transforms
print Meshes().get(Parents)

# skinned meshes 
print SkinClusters().get(Future).only(Meshes).distinct()

#skinned skeleton roots
print SkinClusters().get(History).only(Joints).get(AllParents).only(Assemblies)


# a table of camera focal legnths
cams, lengths = Cameras().split(2)
lengths = lengths.get(Attribute, 'focalLength').get(Values)
print dict ( cams.get(Parents).short().join(focal_length = lengths))

# basic filtering
above = Transforms().where(item.ty > 0)
below = Transforms().where(item.ty < 0)

# no intersection!
assert not any(above & below)

# but ttogether...f
print above + below

# use sets to get an ik chain from a handle:
def ik_chain(handle):
    h = using(handle).get(History).cache()
    down = h.only(Joints).append(AllChildren)
    up = h.only(IkEffectors).append(AllParents)
    return up & down



# chained filtering
used_to_be_cubes = Everything().only('polyCreator').like('cube').get(Future).only(Meshes)
has_8_verts = lambda p: cmds.polyEvaluate(p, v=True) == 8
still_are_cubes = used_to_be_cubes.where(has_8_verts)
print still_are_cubes

# rename using foreach()
print Selected().foreach( lambda p: cmds.rename(p, 'renamed#')).long()

# iterating over a query directly:
for each in Transforms():
    print each, cmds.xform(each, q=True, bb=True)

# turn a query into a list:
ortho_cameras = list(Cameras().where_not(item.orthographic == True).short())
print ortho_cameras

# use uuids to survive a rename
original = DagNodes(cmds.polyCube()).only(Transforms).uuid().cache()
print "was",  original.long()
cmds.select(*DagNodes(original)) # note asterisk!
print "became", cmds.rename("renamed_object")
print  "is", original.long()

# find empty groups
empty_groups = Transforms().where_not(lambda p: any(using(p).get(Children)))
print "empty groups:",  list(empty_groups)
