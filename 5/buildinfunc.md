 
###map(function, iterable, ...)

    Apply function to every item of iterable and return a list of the results.


###Example

    items = [1, 2, 3]
    print items

    def mf(x):
        return x**2

    result = map(mf,items)
    print result


### With lambda function

    items = [1, 2, 3]
    lm = lambda x: x**2
    l = map(lm, items)
    print l

    l = map(lambda x: x**2, items)
    print l


### Output

    [1, 2, 3]
    [1, 4, 9]


    words = ['It', 'is', 'raining', 'cats', 'and', 'dogs'] 
    lengths = map(lambda word: len(word), words)

    >> [2, 2, 7, 4, 3, 4]



###filter(function, iterable)

Construct a list from those elements of iterable for which function returns true. 


    lst = [1,2,3,4,5,6,7,8,9]
    def myf(x):
        if x%2 == 0:
            return True
        else:
            return False

    res = filter(myf,lst)
    print res

[2, 4, 6, 8]



###enumerate(sequence, start=0)

 Return an enumerate object. Sequence must be a sequence, an iterator, or some other object which supports iteration.


    lst = ['one','two','three']

    for i in range(len(lst)):
        print '%s-%s' % (i,lst[i])


    for i,x in enumerate(lst):
        print '%s-%s' % (i,x)

###class list([iterable])

Return a list whose items are the same and in the same order as iterable‘s items. iterable may be either a sequence, a container that supports iteration, or an iterator object.



    print list()
    print list('abc')
    print list((5,6,7))
    print list({'1':'hi', '2': 'bye'})

###class dict()

Dict. With this built-in function, we can construct a dictionary from a list of tuples. The tuples are pairs. They each have two elements, a key and a value.

    # Create list of tuple pairs.
    # ... These are key-value pairs.
    pairs = [("cat", "meow"), ("dog", "bark"), ("bird", "chirp")]

    # Convert list to dictionary.
    lookup = dict(pairs)

    # Test the dictionary.
    print lookup


###Output

    {'bird': 'chirp', 'dog': 'bark', 'cat': 'meow'}



###tuple([iterable])

Return a tuple whose items are the same and in the same order as iterable‘s items.

    tuple([1, 2, 3]) returns (1, 2, 3)

   



