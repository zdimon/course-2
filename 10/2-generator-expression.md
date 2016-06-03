##Generator expressions

Sequence collection is created eagerly, but generator function is lazy.
Items in the collection aren't ceated until they demanded by a for loop
or a function that created a collection like list(), tuple(), set().  

    (expression for varible in source if condition)

    [x for i in range()]
