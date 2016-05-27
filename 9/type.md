##Type function

http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example


With one argument, return the type of an object. 

The isinstance() built-in function is recommended for testing the type of an object.

With three arguments, return a new type object.

    type('mycls',(object,),dict(a=1))

This is essentially a dynamic form of the class statement.

###Class can be created at runtime!!!

    def make_myklass(**kwattrs):
        return type('MyKlass', (object,), dict(**kwattrs))

### Question

    type(object)

Our class is equivalent this:

    class MyKlass(object):
      foo = 2
      bar = 4


A metaclass is defined as "the class of a class". 
Any class whose instances are themselves classes, is a metaclass.

Since a metaclass is the class of a class, it is used to construct classes 
(just as a class is used to construct objects). 


what Python does under the hood when it sees class:

When it sees a class definition, Python executes it to collect the attributes (including methods) 
into a dictionary.
When the class definition is over, Python determines the metaclass of the class. 
Let's call it Meta
Eventually, Python executes Meta(name, bases, dct), where:

- Meta - is the metaclass
- name - is the name of the newly created class
- bases - is a tuple of the class's base classes
- dct - maps attribute names to objects, listing all of the class's attributes

    MyKlass = type(name, bases, dct)

If we have our own meta class:

    class MyKlass(object):
        __metaclass__ = MyMeta
        foo = 2

It will go like this

    MyKlass = MyMeta(name, bases, dct)

So MyMeta should be implemented appropriately to support such calling form and return the new class.
It's actually similar to writing a normal class with a pre-defined constructor signature.

##New and init constructor

To controll creation and inicialization of the class in the metaclass 
we have __init__ and __new__ methods (constructors).

new - creation object
init - initialization object after it has been created

##Question what the class we need to set as parent for metaclass?












    class MyMeta(type):
        def __new__(meta, name, bases, dct):
            print '-----------------------------------'
            print "Allocating memory for class", name
            print meta
            print bases
            print dct
            return super(MyMeta, meta).__new__(meta, name, bases, dct)
        def __init__(cls, name, bases, dct):
            print '-----------------------------------'
            print "Initializing class", name
            print cls
            print bases
            print dct
            super(MyMeta, cls).__init__(name, bases, dct)




    class MyKlass(object):
        __metaclass__ = MyMeta

        def foo(self, param):
            pass

        barattr = 2


##Metaclass's __call__

__call__ is called when the already-created class is "called" to instantiate a new object.


    class MyMeta(type):
        def __call__(cls, *args, **kwds):
            print '__call__ of ', str(cls)
            print '__call__ *args=', str(args)
            return type.__call__(cls, *args, **kwds)

    class MyKlass(object):
        __metaclass__ = MyMeta

        def __init__(self, a, b):
            print 'MyKlass object with a=%s, b=%s' % (a, b)

    print 'gonna create foo now...'
    foo = MyKlass(1, 2)





