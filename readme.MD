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
q = Scene(['top'])
```

This would produce a query object (technically a `minq.Stream` object)  -- but as of yet it has no results: it's a description  of a query you  _could_ call,  not a list of objects.

To get the result call its `.execute()`  function:

```python
print q.execute()
[u'|top']
```

but the main use pattern is to iterate over it: the query is automatically executed when you try to loop over it:

```python
q = Scene(['top', 'front'])
for item in q:
    print item

# u'|top'
# u'|front'
```

It's often  convenient to turn the results directly into a list or a tuple:

```python
tuple(Cameras())
# Result: (u'frontShape', u'perspShape', u'sideShape', u'topShape') # 

list(Scene().only('polyCreator'))
# Result: [u'polyCube1', u'polyCube2', u'polyCube3', u'polyUnite1'] # 
```

You can also check for contents using built in python checks like `in`, `any`, or `all`:

```python
u'|top' in Cameras()
# True

u'|pCube1' in Cameras()
# False

any(Meshes().like('cube'))
# True
```

Doing this runs the query, of course, but it's a readable way to make it clear what you're really hunting for.


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

At the risk of being repetitive: a stream is not a function that returns a list: its an object that can be iterated over to perform a particular search in the maya scene.

Ordinarily the last item in a query chain is determines the results. For example

```python
Selected().only(Transforms)
```
will give you the selected transforms, but not their shapes.  The `append()` function will add the results of a new query operation to an existing stream:  So 

```python
Selected(),only(Transforms).append(AllChildren)
```
Will give you the selected transforms _and_ all of their children, including shapes. For more complex combinations of queries you can also use *set operations* (see below).

Occasionally you'll want to start a query with one or more objects whose names you already know, In that case the `using()` function creates a stream with whatever objects you pass in explicitly. For exaample:

```python
using("character_root").get(AllChidren).only(IKHandles)
```

will return all of the ik handles under `character_root`.   `using` accepts multpile arguments if you want to start the query with multiple objects.


Filtering
-------

A lot of scene query involves whittling down to a smaller set of results. There are three main ways to filter a list of objects in minq:

.like()
-----

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
------

The `.only()` function limits the contents of a stream to one or more particular kinds of Maya objects.  It's almost identical to calling `cmds.ls()` on a list of strings. Thus:

```python
some_stream.only('camera','light')
```

will return all the camera and light nodes in `some_stream`.  Note that this is a type match and not a name match -- it's equivalent to

```python
cmds.ls(list_of_nodes, type =('camera', 'light'))
```

For convenience, minq includes subclasses of Stream dedidcated to particular Maya node types:  `Cameras()` and `Meshes()` mentioned above are examples.  You can used these classes to start a stream containing all the objects of a particular type:

```python
Meshes().like("house_mesh")
```

or you can pass them to  the `.only()` function for use as filters: thus

```python
some_stream.only(Meshes, Cameras)
```
is equivalent to 

```python
some_stream.only('mesh', 'camera')
```

This is usually significantly faster than piecewise methods like checking maya's `nodeType()` function on objects one at a time.

`only()` also supports a keyword parameter to specify a namespace. If used, it will limit the stream to only items in the supplied namespace.  You can specify a namespace using either partial or complete namespaces.  A partial namespace argument will match any namespace containing the name you supply thus:

```python
Transforms().only(namespace = 'test')
# Stream(['|test:pCube1',  '|nested:test:pCube1'])
```
A complete namespace begins with a leading colon and only matches the exact namespace.  Thus:

```python
Transforms().only(namespace=':test')
# Stream(['|test:pCube1'])  # 'nested:test is' excluded
Transforms().only(namespace=':nested:test')
# Stream(['|nested:test:pCube1'])  # 'test' is excluded
```

The namespace flag can be combined with other `only()` specifiers, such as `DagNodes().only('skinClusters', namespace="export")`.

.where()
--------

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

Since calling a function on every item in a long stream can be very expensive, minq includes a facilty for doing one common class of tests in bulk.  minq includes a special class called `item` (note the casing!) which generates queries on attributes.  For example:

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

`where()` also comes in the form `where_not()`, which works in the same fashion but negates the test -- this helps you avoid writing a lambda just to invert a test function.

Expanding and transforming
--------

Some operators change the data which is passing through, rather than filtering a stream of values as they fly by.  For example, you can convert a list of shapes into a list of transforms, of get all of the nodes in the history of your current stream.  In minq this is done with the `get()` function and a series of classes which apply these transfomations streams.  Here are a few examples:

```python
camera_transforms = Cameras().get(Parents)
# Result: Stream([u'|front', u'|persp', u'|side', u'|top']) # 

sphere_history = Meshes().like('sphere').get(History)
# Result: Stream([u'|pSphere1|pSphereShape1', u'polySphere1']) # 

skinned_meshes = Scene().only('skinCluster').get(Future)
# Result: Stream([u'|characterMesh|characterMeshShape']) # 
```

Some `get()` operations don't produce object names.  For example:

```python
mesh_translates = Meshes().get(Parents).get(Attribute, 't').get(Values)
# Result: Stream([(0,0,0), (10,0,0), (0,20.2123, 11)]) # 
```

where `Attributes` is a Stream type that turns object names into `object.attribute` names and `Values` runs a maya `getAttr` on a stream of values -- this is a fast way to query for all of the values on a particular set of attributes in bulk with a single maya call, much quicker than iterating over a list can calling `getAttr` many times.

You can also use the `.foreach()` function to produce streams from arbitrary functions run on a stream.  A simple but useless example might be:

```python
print Cameras().short().foreach(lambda p: p.upper())
# Stream([u'FRONTSHAPE', u'PERSPSHAPE', u'SIDESHAPE', u'TOPSHAPE'])
```

foreach can be  used for sophisticated filtering or transformations: for example:

```python
def connected_shaders(object):
    sgs = cmds.listConnections(object, type='shadingEngine') or []
    return tuple(set( cmds.listConnections(*sgs, type = 'lambert') or []))

print Meshes().foreach(connected_shaders)
# Result: Stream([(u'lambert1',), (u'blinn1',), (u'lambert1', u'phong1')]) # 

```

Tables
------
Sometimes you'll want to collect information in a tabular format: list all of the object's positions by object, for collect all of the shaders attached to meshes in the previous examples.  Streams offer a tabulating function called '.join()' which allows you to merge multiple streams into a single stream of 'rows' -- as long as all of the streams line up the result is effectively a table.  

For example, the `connected_shaders` function above returns the shaders for each mesh -- but not the meshes themselves.  However you can get the data in a more useful format using `.join()`:

```python
mesh_stream = Meshes()
shader_stream = mesh_stream.foreach(connected_shaders)
table = mesh_stream.join(shaders = shader_stream)
for each_row in table:
    print each_row

# dataRow(index=u'|pCube1|pCubeShape1', shaders=(u'lambert1',))
# dataRow(index=u'|pPyramid1|pPyramidShape1', shaders=(u'blinn1',))
# dataRow(index=u'|pSphere1|pSphereShape1', shaders=(u'lambert1', u'phong1'))
```

Since the 'dataRows' are really just namedtuples, you can also convert them to dictionaries:

```python
print dict(table)
{u'|pCube1|pCubeShape1': (u'lambert1',), u'|pPyramid1|pPyramidShape1': (u'blinn1',), u'|pSphere1|pSphereShape1': (u'lambert1', u'phong1')}
```

This example is not particularly optimized, because both `mesh_stream` and `shader_stream` will execute the original `Meshes()` query.  In performance-intensive situations you could avoid exdcuting the query again by using the `.split()` function of a Stream to split the Meshes() call into two:

```python
meshes, shaders = Meshes().split(2)
m = meshes.join(shaders= shaders.foreach(connected_shaders))
dict(m)
# {u'|pCube1|pCubeShape1': (u'lambert1',), u'|pPyramid1|pPyramidShape1': (u'blinn1',), u'|pSphere1|pSphereShape1': (u'lambert1', u'phong1')}

```

This version will perform better because `split()` will not force multiple evaluations of the same query.

Grouping
-----------
It is often useful to be able to group the data in a stream. For example, you might have a stream containing a set of meshes and you like to sort them into high, medium and low poly-count groups.  The `group_by()` operator allows you to subset a stream into groups of related items:

```python
def poly_category(obj):
    count = cmds.polyEvaluate(obj, v=True)
    if count > 512: return 'high'
    if count > 256: return 'med'
    return 'low'

for category, meshes in Meshes().group_by(poly_category):
    print category, ":", meshes
    
# high : [u'|pHelix1|pHelixShape1']
# med : [u'|pSphere1|pSphereShape1', u'|pSphere2|pSphereShape2']
# low : [u'|pCube1|pCubeShape1']
```

If the incoming stream consists of `dataRows` you can pass an integer or string key to select based on the appropriate 'column' in the dataRows, rather than a grouping function.  


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

(q ^ o).execute() # XOR : Items not in both sets
# Result: (u'|persp|perspShape',) # 
```

This can be an economical way of doing big operations in bulk instead of using for-loops, and it's also a clear way of expressing ideas like _I an looking for an object which is both a shape and a child of this assembly_ or _I am looking for a mesh which is not skinned and not templated_.

Installation
------------
Minq is a standard python package with no dependencies. place the minq folder where it will be found on your python path. The module id designed to be star-imported, though you can do limited imports if you preefer.
 
Licensing
-----------
This project is provided unter the MIT license: you're free to use as you like, providing you retain the copyright information in `minq.__init__.py`
