##Python descriptors

Descriptors are objects with any of __get__, __set__, or __delete__. 
These descriptor objects can be used as attributes 
on other object class definitions.

1. Consider a program in which we need to enforce strict 
type checking for object attributes. 
Python is a dynamic languages and thus does 
not support type checking.


2. Consider a program in which we want to create 
attributes that are initialized once at run-time 
and then become read-only.


3. Finally, imagine a program in which we wanted 
to somehow customize object attribute access.


        def __init__(self, num, max):
            self.max = max
            self.num = num


        def __get__(self, instance, cls):
            print 'getting number'
            return self.num

        def __set__(self,instance,value):
            print 'trying to set number %s' % value
            if value>self.max:
                raise TypeError("Must be less then %s" % self.max) 
            self.num = value

        def __delete__(self,instance):
            raise AttributeError("Can't delete attribute")

    class Account(object):
        number = Mynumber(3,10)
        

    aa = Account()

    import pdb; pdb.set_trace()

