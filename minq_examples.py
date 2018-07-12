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

# a table of camera focal lengths
cams, lengths = Cameras().split(2)
lengths = lengths.get(Attribute, 'focalLength').get(Values)
print dict ( cams.get(Parents).short().join(focal_length = lengths))

# basic filtering
above = Transforms().where(item.ty > 0)
below = Transforms().where(item.ty < 0)

# no intersection!
assert not any(above & below)

# but together...
print above + below

# use sets to get an ik chain from a handle.  Here we use 'cache'
# to avoid calling the history twice
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

# find nulls with no shape children
no_shapes = Transforms().where_not(lambda p: any(using(p).get(AllChildren).only(Shapes)))
print "no shape kids:", list(no_shapes)

# get the type of the selection, accounting for shape children too:
selected_type = Selected().append(Children).foreach(cmds.nodeType)
# so you can see if a mesh is selected like
'mesh' in Selected().append(Children).foreach(cmds.nodeType)

# ... although a better way to do the same thing would be
any(Selected().append(Children).only(Meshes))

# find meshes with multiple UV sets
multiple_uvs = Meshes().where(lambda p: using(p).get(UVSetCount).first() > 1)
print "meshes with multiple UVs:", list(multiple_uvs)

#find meshes with no UVs
no_uvs = Meshes().where_not(lambda p: using(p).get(UVPointCount).first())
print "meshes with no uvs:", list(no_uvs)

# get the contents of a display layer
plain_contents = DisplayLayers().like('layer_name').get(Future).only(DagNodes)

# display layers can contain a mix of shapes and transforms; get 
# the parents of any shapes and the children of any transforms.  This
# will be equivalent to the _visual_ impact of the layer assignments.
# Use the 'split' feature to branch the original query into 3 streams
results, xforms, shapes = DisplayLayers().like('layer_name').get(Future).only(DagNodes).split(3)
print "layer contents", list(results + xforms.get(AllChildren) + shapes.only(Shapes).get(Parents))

# filter to a namespace
Meshes().only(namespace='some_namespace')

# ...or to a nested namespace:
Meshes().only(namespace='parent:child')

# ...or an absolute namespaces (starting from root)
Meshes().only(namespace=':parent:child')

# you can also specify a namespace to start a query with 'using':
# this form supports wildcards in the namespace paths and is 
# not inclusive, so you can get a namespace without its children

using("some_namespace:*")
using(":parent:*")   # will not get 'child'









