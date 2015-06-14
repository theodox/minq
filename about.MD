a simple query language for Maya scenes

The query system allows for lazy execution a maya command (usually ls, but this change in derived classes) and iteration over thew results:

A simple example:

    q = QueryBase('top*')

produces a query object -- but as of yet it has no results: it's a description of a query you _could_ call, not a list of objects

To get the result call it directly:

    print q.results()
    [u'|top', u'|top|topShape']

iterating over the results also calls the query:

   for item in q:
       print item

   |top
   |top|topShape

This class and its derivatives use the QueryMeta metaclass so they can specify command flags cleanly: most derived classes differ only in flags

Queries can be chained together. All QueryMeta classes can 'chain' to other types, creating a cascading filter that will be evaluated only
when called: For example:

   q = Query().Transforms.Filter('fred').WithChildren

would find all the transforms in the scene with 'fred' in their names who have children, while

    q = Query('joint1').Children.Shapes

would find all of the children of 'joint1' which are shapes.  As with a simple query, the actual values are not
retrieved until the query is iterated or results are called


operations
===========

Queries can be treated like sets (the set operations, like the queries, will be evaluated lazily when the results are requested or iterated). So you, for example:


    cube_parents  = Nodes().OfType('polyCube').Parents
    lights = Nodes.OfType('light')
    
    combined = cube_parents + lights
    for item combined:
        print item
    
    |pCube1
    |ambientLight1|ambientLightShape1
    
Queries can be combined as followed:
 