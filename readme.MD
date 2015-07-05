minq
-----
A query language for Maya scenes
======================================

This project aims to cut down on the large amount of boilerplate involved in finding objects in a Maya scene.  There 
are several commands -- `ls()`, `listRelatives()` and `listHistory()` are the most obvious but not the only ones 
which have to work together when you're attempting to find an object in a maya scene. For example, if you wanted to 
find all the IK handles attached to right the right hand (but not the right foot) of a character in your scene  you'd
 have to try something like:
 
    iks = cmds.ls(type = 'ikHandle') or []
    for ik in iks:
        parents = cmds.listRelatives(ik, p=True)
        for p in parents:
            if p.split("|")[-1] == 1:
                return p
    return None
    
Which is a bit much for such a simple idea. It's particularly annoying because different commands use slightly 
different result formats:  you need to remember to  `or []` after `ls()` so you can iterate the results; you if you 
want unambiguous paths `ls` expects the `long` flag but `listRelatives` uses `fullPath` for the same thing.

The goal of minq is to provide a less wordy and more declarative way to look for things in the maya scene.  The idea 
is that you state your goals up front and then execute them at once, rather than creating and storing intermediate 
results. This is both faster to execute and also cleaner to read.

The key is that the queries are _not_ commands: they are descriptions of commands you'll run in sequence. The 
simplest query is no different from an `ls()` call:

    q = scene('top*')

This would produce a query object (tecnically a `minq.Expression` object)  -- but as of yet it has no results: it's a 
description  of a query you  _could_ call,  not a list of objects.

To get the result call it directly:

    print q.eval()
    [u'|top', u'|top|topShape']

It's often more convenient to turn the results directly into a list or a tuple:

    tuple(cameras())
    # Result: (u'|front|frontShape', u'|persp|perspShape', u'|side|sideShape', u'|top|topShape') # 
 
    list(nodes().of_type('polyCreator'))
    # Result: [u'polyCube1', u'polyCube2', u'polyCube3', u'polyUnite1'] # 

Iterating over the results also calls the query:

    for item in q:
        print item

    |top
    |top|topShape

Query chaining
===============


The real power of this setup is that the expressions can be expanded in place without loops and temporary variables. 
This works quite similarly to [linq](https://msdn.microsoft.com/en-us/library/bb397906.aspx), or the database query 
system in [peewee](https://github.com/coleifer/peewee): rather than creating a series of operations and storing the 
intermediate results you create a chain of operations that can be optimized and evaluated at once.

In minq, the `minq.ExpressionMeta` metaclass allows you to chain conditions off any expression instance. A simple 
example might be

    meshes().parents.like('wall')
    
which would find all the meshes in the scene whose parents were named "*wall*".  Under the hood that expression would
 translate to something like:
 
    results = []
    meshes = cmds.ls(type='mesh') or []
    if meshes: 
        parents = cmds.listRelatives(*meshes, p=True)
        for item in parents:
            if re.match('wall', item):
                results.append(item)
    return results

Minq will try to optimize the conditions yu provide. Often different operations are variants on the same maya command
(usually, but not always, `ls()`). Where possible minq will combine the flags on flags on successive queries for a
speedied execution: so a series of queries based on the maya `ls()` command will be reduced to a single function. 
Thus:

    scene().of_type('mesh').of_type('light').of_type('camera') 

will result in a single call : `cmds.ls(type = ('mesh', 'light', 'camera')`

More often, though, the chaining of the results is ussed to filter the results down to a subset:

    q = transforms().like('fred').leaves

would find all the transforms in the scene with 'fred' in their names who have no children, while

    scene('joint1').children.shapes

would find all of the children of 'joint1' which are shapes.  As with a simple query, the actual values are not
retrieved until the query is iterated or results are called.


Filtering
==========

Many operators act as 'filters', whittling down a set of results to a smaller and smaller group.  While

    scene()
   
will return everything (it's effectively `cmds.ls`), 

    scene().meshes
    
will return only mesh nodes.  

Besides type filters you can use arbitary filter expressions. The simplest are `like` and `unlike`, which use regular
 expressions to filter objects on names:
 
    cameras().like('top').eval()
    # Result: (u'|top|topShape',) # 

    # return cameras with no 'o' in their name
    cameras().unlike('o').eval():
    # Result: (u'|persp|perspShape', u'|side|sideShape') # 

By default both `like` and `unlike` are case sensitive, but you can pass any regex arguments to make them ignore case:
```python
    cameras().like('TOP').eval()
    # Result: () # 
    
    cameras().like('TOP', re.I)
    # Result: (u'|top|topShape',) # 
```
Since like and unlike are regexes you can use python regex controls for more control:

    # use the regex square brackets to find multiple possibilities
    transforms().like('pCube[1,2]').eval()
    # Result: (u'|pCube1', u'|pCube2') # 

The most general filter expressions are `where` and `where_not`, which allow you to pass in an arbitrary function 
that takes a single maya object as an argument. Any item where that function returns a True value will be passed.  
For example:

     above_ground = lambda p: cmds.getAttr(p + ".ty") > 0
     transforms().where(above_ground).eval()
     # Result (u'|high_cube',) #
     
`where` takes positive results from the function and `where_not` passes negative results:

     above_ground = lambda p: cmds.getAttr(p + ".ty") > 0
     transforms().where_not(above_ground).eval()
     # Result (u'|low_cube',) #

For the very common maya case of checking attribute values, there is a special expression named `item` which allows 
you to write simple attribute checks easily.  The last example can be written more neatly as:

    transforms().where(item.ty > 0)
    
under the hood the expression 'item.ty > 0' creates a callable function which is essentially:

    def item_test(maya_object):
        value = cmds.getattr(object + ".ty")
        return value > 0
        
Naturally this can cause issues if the item does not have a 'ty' attribute.  By default the item - attribute tests 
will simply fail if the required attribute is not present. If you want see the exceptions, you can use the 'strict' 
flag so that bad queries raise exceptions.  So:

    unsafe_query = item.ty > 0
    unsafe_query.strict = True
    cameras().where(unsafe_query).eval()
    # Error: ValueError: file minq/minq/minq/item.py line 41: No object matches name: |front|frontShape.ty # 

The actual logic is in `items.py`.  When in doubt you can use a regular function, the item syntax is intended as a 
convenience for common cases and not the answer to all possible problems.


Expanding and transforming
==========================

Some operators change the data which is passing through, something like what happens in a SQL 'cast' statement.  A 
simple and not very useful example:

    upper_case = lambda p: p.upper()
    q = cameras().parents.cast(upper_case)
    # Result: (u'|FRONT', u'|PERSP', u'|SIDE', u'|TOP') # 

The argument to cast is a single-item function which will be called on every item in the query.  Note that -- unlike 
regular queries -- this can produce results which don't exist in the maya scene.  The operators which can apply these
 kind of arbitrary changes to the data are grouped together in the `minq.projections` submodule.

`cast()` is completely general, but there are several more targeted transformations you  can apply to the query 
for common maya operations.  For example:

    meshes().parents.translations.eval()
    # Result: ((u'|pCube1', XYZ(x=0.0, y=0.0, z=0.0)), (u'|pPlane1', XYZ(x=0.0, y=2.0, z=0.0)), (u'|pSphere1', XYZ
    (x=-2.5, y=1.25, z=1.0))) # 

will give you a list of object - XYZ tuple pairs for all of the mesh transforms in the scene. Many of the projection 
operators return (name, value) pairs like `translations()` so that you can turn the results into a dictionary:

    dict(cameras().parents.translations())
    # Result: {u'|side': XYZ(x=350, y=50, z=5), 
               u'|top': XYZ(x=-35, y=200, z=0), 
               u'|persp': XYZ(x=280, y=80, z=370), 
               u'|front': XYZ(x=60, y=70, z=140 )} # 


Set Operations
===========

Queries can be treated like sets.  So, for example:


    cube_parents  = nodes().of_type('polyCube').parents
    red_lights = lights().where(item.colorR > .5).where(item.colorG < .5)
    
    combined = cube_parents + lights
    for item combined:
        print item
    
    |pCube1
    |ambientLight1|ambientLightShape1
    
Like the queries, the set operations will be evaluated only when called. The sets can be combined with the same 
operators as python sets:

    q = cameras()                                   # all cameras
    o = cameras().where(item.orthographic == True)  # only ortho cameras

    (q | o).eval() # union:
    # Result: (u'|side|sideShape', u'|top|topShape', u'|front|frontShape', u'|persp|perspShape') # 
           
    (q & o).eval() #intersection  -- in both sets
    # Result: (u'|side|sideShape', u'|top|topShape', u'|front|frontShape') # 
    
    (q - o).eval() # difference --  in q but not in o
    # Result: (u'|persp|perspShape',) # 
    (o - q).eval() # difference is order dependent!
    # Result: (,) # 

    (o ^ q).eval() # symmetric difference -- non-overlapping
    # Result: (u'|persp|perspShape',) # 

This can be an economical way of doing big operations in bulk instead of using for-loops.

 
