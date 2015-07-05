a simple query language for Maya scenes

The query system allows for lazy execution a maya command (usually ls, but this change in derived classes) and iteration over thew results:

A simple example:

    q = scene('top*')

produces a query object -- but as of yet it has no results: it's a description of a query you _could_ call, not a list of objects

To get the result call it directly:

    print q.eval()
    [u'|top', u'|top|topShape']

iterating over the results also calls the query:

    for item in q:
        print item

    |top
    |top|topShape

This class and its derivatives use the ExpressionMeta metaclass so they can specify command flags cleanly: most derived classes differ only in flags. The system will attempt to combine flags on similar queries for a speedied execution: so a series of queries based on the maya `ls()` command will be reduced to a single function:

    scene().of_type('mesh').of_type('light').of_type('camera') 

will result in a single call : `cmds.ls(type = ('mesh', 'light', 'camera')`

Queries can be chained together, filtering the original results down to a subset. 


    q = transforms.like('fred').leaves

would find all the transforms in the scene with 'fred' in their names who have no children, while

    q = scene('joint1').children.shapes

would find all of the children of 'joint1' which are shapes.  As with a simple query, the actual values are not
retrieved until the query is iterated or results are called.

Expanding and transforming
==========================

Some operators change the data which is passing through, something like what happens in a SQL 'cast' statement.  A 
simple example:

    upper_case = lambda p: p.upper()
    q = cameras().parents.cast(upper_case)
    # Result: (u'|FRONT', u'|PERSP', u'|SIDE', u'|TOP') # 

The argument to cast is a single-item function which will be called on every item in the query.  Note that -- unlike 
regular queries -- this can produce results which don't exist in the maya scene.

There are several other transformations you can apply to the query for common operations.  For example:

    meshes().parents.translations.eval()
    # Result: ((u'|pCube1', XYZ(x=0.0, y=0.0, z=0.0)), (u'|pPlane1', XYZ(x=0.0, y=2.0, z=0.0)), (u'|pSphere1', XYZ
    (x=-2.5, y=1.25, z=1.0))) # 


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
    
    cameras().like('TOP').eval()
    # Result: () # 
    
    cameras().like('TOP', re.I)
    # Result: (u'|top|topShape',) # 

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

 
