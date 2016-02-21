minq
====
A query language for Maya scenes
-----

This project aims to cut down on the large amount of boilerplate involved in finding objects in a Maya scene.  There 
are several commands -- `ls()`, `listRelatives()` and `listHistory()` are the most obvious but not the only ones 
which have to work together when you're attempting to find an object in a maya scene. For example, if you wanted to 
find all the IK handles attached to right the right hand (but not the right foot) of a character in your scene  you'd
 have to try something like:

```python 
iks = cmds.ls(type = 'ikHandle') or []
for ik in iks:
    parents = cmds.listRelatives(ik, p=True)
    for p in parents:
        if p.split("|")[-1] == 1:
            return p
return None
```

Which is a bit much for such a simple idea. It's particularly annoying because different commands use slightly different result formats:  you need to remember to `or []` after `ls()` so you can iterate the results; you if you 
want unambiguous paths `ls` expects the `long` flag but `listRelatives` uses `fullPath` for the same thing.

The goal of minq is to provide a less wordy and more declarative way to look for things in the maya scene.  The idea is that you state your goals up front and then execute them at later, rather than creating and storing intermediate 
results. This is both faster to execute and also cleaner to read.

The key is that the queries are _not_ commands: they are descriptions of commands you'll run in sequence. The  simplest query is no different from an `ls()` call:

```python
q = Scene('top*')
```

This would produce a query object (technically a `minq.Stream` object)  -- but as of yet it has no results: it's a 
description  of a query you  _could_ call,  not a list of objects.

To get the result call it directly:

```python
print q.execute()
[u'|top', u'|top|topShape']
```
It's often more convenient to turn the results directly into a list or a tuple:
```python
tuple(Cameras())
# Result: (u'frontShape', u'perspShape', u'sideShape', u'topShape') # 

list(Scene().only('polyCreator'))
# Result: [u'polyCube1', u'polyCube2', u'polyCube3', u'polyUnite1'] # 
```

Iterating over the results also calls the query:
```python

for item in Cameras():
    print item

# frontShape
# perspShape
# sideShape
# topShape
```

Query chaining
-----

The real power of this setup is that the expressions can be expanded in place without loops and temporary variables.  This works quite similarly to [linq](https://msdn.microsoft.com/en-us/library/bb397906.aspx), or the database query 
system in [peewee](https://github.com/coleifer/peewee): rather than creating a series of operations and storing the intermediate results you create a chain of operations that can be optimized and evaluated at once.

In minq, the `minq.Stream` class and its derivatives allow you to chain conditions off any expression instance. A simple  example might be

```python
Meshes() # get all the polyMesh nodes in the scene
Meshes().get(Parents)  # get the immediate parents of all the meshes in the scene
Meshes().get(Parents).like('wall')  # get all mesh parents with 'wall' in their names
```

which would find all the meshes in the scene whose parents were named "*wall*".  Under the hood that expression would translate to something like:

```python
results = []
meshes = cmds.ls(type='mesh') or []
if meshes: 
    parents = cmds.listRelatives(*meshes, p=True)
    for item in parents:
        if re.search('wall', item):
            results.append(item)
return results
```

As with a simple query the chained query *does not actually evaluate* until is iterated or executed. It will re-evaluate when called again:

```python
cubes = Meshes().get(Parents).like('cube')
print cubes.execute()
# [u'pCube1']
cmds.polyCube()
print cubes.execute()
# [u'pCube1', u'pCube2']
```

In other words a stream is not a function that returns a list: its an object that can be iterated over to perform a particular search in the maya scene.

Filtering
-------

A lot of scene query involves whittling down to a smaller set of results. There are three main ways to filter a list of objects in minq:

.like()
====

The `like()` function of a stream is a regex filter: it will pass every incoming value which matches the supplied text expression.

```python
print Cameras()  # Cameras() is a stream object 
# Stream([u'frontShape', u'perspShape', u'sideShape', u'topShape'])

print Cameras().like('top')
# Stream([u'topShape'])
```
 
`like()` is similar to the wildcard functionality in `cmds.ls` but it has two important differences.
  
First, it defaults to a *subset* match rather than a full patch, and it is *case insensitive*. In the example above, 'top' matches 'topShape' without the need for an additional "*".  If you're trying to do exact matches you can add the exact flag:  

```python
print Cameras().like('top', exact=True)
# Stream([])
```

Second, like uses full regular expressions, so you can do things like this:

```python
print Joints().like('Left(hand|foot)$')
# Result: Stream([u'Character1_LeftFoot', u'Character1_LeftHand']) 
```

which will match `Character1_LeftHand`  but not `Character1_LeftHandIIndex1`.

.only()
======

The `.only()` function limits the contents of a stream to one or more particular kinds of Maya objects.  It's almost identical to calling `cmds.ls()` on a list of strings. Thus:

```python
some_stream.only('camera','light')
```

will return all the camera and light nodes in `some_stream`.  Note that this is a type match and not a name match -- it's equivalent to

```python
cmds.ls(list_of_nodes, type =('camera', 'light'))
```

For convenience, the submodule `minq.nodes` includes subclasses of Stream dedidcated to particular Maya node types:  `Cameras()` and `Meshes()` mentioned above are examples.  You can used these classes to start a stream containing all the objects of a particular type:

```python
Meshes().like("house_mesh")
```

or you can pass them to  the `.only()` function: thus

```python
some_stream.only(Meshes, Cameras)
```
is equivalent to 

```python
some_stream.only('mesh', 'camera')
```

.where()
=========

For more complex filtering you'll want to run tests on all of the contents in a stream. In typical Maya programs you'd do something like this:

```python
# get all the meshes whose translateX is larger than 50
result = []
for item in cmds.ls(type = mesh):
    parent = cmds.listRelatives(item, p=True)[0]
        if cmds.getAttr(parent + ".tx") > 50:
            result.add(parent)
```

The minq equivalent to this kind of filtering is the `.where()` function. `.where()` takes a callable argument and applies it to every item in the stream, passing only those for which the callable returns a truthy value:

```python
tx_over_fifty = lambda p: cmds.getAttr(p + ".tx") > 50
Meshes().get(Parents).where(tx_over_fifty)
```

The callable argument to where() can be any callable object that takes one argument (the item in the stream) and returns a value that can be truth tests.  For example you could find connected nodes like this:

```
Scene().where(cmds.listConnections)
```

because `listConnections` returns an empty list for objects with no connections, so unconnected objects won't pass the filter (it's probably not good practice to rely on this behavior here because the intent of the code is not very explicit, however).  

Since calling a function on every item in a long stream can be very expensive, minq includes a facilty for doing one class of tests in bulk.  minq includes a special class called `item` (note the casing!) which generates queries on attributes.  For example:

```python
tx_over_fifty = lambda p: cmds.getAttr(p + ".tx") > 50
Meshes().get(Parents).where(tx_over_fifty)
```

is equivalent to

```python
Meshes().where(item.tx > 50)
```

under the hood `item.tx > 50 ` is evaluated to produce an anonymous callable function that does the same test as the lammbda: in fact you can use it without `where`

``` python
test = item.tx > 50
print test('pCube1')
# False
```

More importantly, using the item class to generate this kind of query tells minq to bundle up all of the `getAttr` commands in a single call, rather than issuing them one at a time. This significantly speeds up large queries.  When in doubt, of course,  you can still use a regular function, the item syntax is intended as a  convenience for common cases and not the answer to all possible problems.


Expanding and transforming
--------

Some operators change the data which is passing through, rather than filtering a stream of values as they fly by.  For example, you can convert a list of shapes into a list of transforms, of get all of the nodes in the history of your current stream.  In minq this is done with the `get()` function and a series of classes which apply these transfomations streams.  Here are a few examples:

```python
camera_transforms = Cameras().get(Parents)
# Result: Stream([u'front', u'persp', u'side', u'top']) # 

sphere_history = Meshes().like('sphere').get(History)
# Result: Stream([u'pSphereShape1', u'polySphere1']) # 

skinned_meshes = Scene().only('skinCluster').get(Future)
# Result: Stream([u'characterMeshShape']) # 
```

You some `get()` operations don't produce object names.  For example:

```python
mesh_translates = Meshes().get(Parents).get(Attribute, 't').get(Values)
# Result: Stream([(0,0,0), (10,0,0), (0,20.2123, 11)]) # 
```


** this section needs expansion **


Set Operations
-------

Queries can be treated like sets.  So, for example:

```python
cube_parents  = nodes().of_type('polyCube').parents
red_lights = lights().where(item.colorR > .5).where(item.colorG < .5)

combined = cube_parents + lights
for item combined:
    print item

# |pCube1
# |ambientLight1|ambientLightShape1
```    
Like the queries, the set operations will be evaluated only when called. The sets can be combined with the same 
operators as python sets:
```python
q = Cameras()                                   # all cameras
o = Cameras().where(item.orthographic == True)  # only ortho cameras

(q + o).execute() # union:
# Result: (u'|side|sideShape', u'|top|topShape', u'|front|frontShape', u'|persp|perspShape') # 
       
(q - o).execute() # difference --  in q but not in o
# Result: (u'|persp|perspShape',) # 

(o - q).execute() # difference is order dependent!
# Result: (,) # 

(q & o).execute() #intersection  -- in both sets
# Result: (u'|side|sideShape', u'|top|topShape', u'|front|frontShape') # 
```

This can be an economical way of doing big operations in bulk instead of using for-loops.

 