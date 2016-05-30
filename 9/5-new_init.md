## New & init

Use __new__ when you need to control the creation of a new instance. 
Use __init__ when you need to control initialization of a new instance.

__new__ is the first step of instance creation. 
It's called first, and is responsible for returning a new instance of your class. 
In contrast, __init__ doesn't return anything; 
it's only responsible for initializing the instance after it's been created.

    class A(object):
        pass

For the class A we did not define __new__ and __init__ method so when we will create our object like this

    o = A()

our class will search __new__ and __init__ method inside parent calss (object) and will have found it inside __dict__ attribute.
    
o=A() is equivalent to:

    a = object.__new__(A)
    object.__init__(a)

Using super we can call methods from the parent class.

##Singleton

    class C(object):
        instance = None
         def __new__(cls):
             if cls.instance is None:
                 cls.instance = super(C, cls).__new__(cls)
             return cls.instance


    >>C() is C()
    >>C().x=1
    ...

