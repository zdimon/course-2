##Static and class methods.


The most used methods in classes are instance methods, i.e instance is passed as the first argument to the method.

For example, a basic instance method would be as follows:

    class Cat(object):
        def __init__(self, sound):
            self.sound = sound
     
        def say(self):
            print(self.sound)
     
    mur4ik = Cat('murrrr')
    mur4ik.say()

### Output

    murrrr

Now what if the method we want to write interacts with classes only and not instances? 
We can code a simple function out of the class to do so but that will spread the code related to class, to out of the class. 
This can cause a future code maintenance problem, as follows:


    def get_no_of_instances(cls_obj):
        return cls_obj.no_inst
     
    class Kls(object):
        no_inst = 0
     
        def __init__(self):
            Kls.no_inst = Kls.no_inst + 1
     
    ik1 = Kls()
    ik2 = Kls()
     
    print(get_no_of_instances(Kls))


### Output

    2



##The Python @classmethod

Using features introduced after Python 2.2, we can create a method in a class, using @classmethod.



    class Kls(object):
        no_inst = 0
     
        def __init__(self):
            Kls.no_inst = Kls.no_inst + 1
     
        @classmethod
        def get_no_of_instance(cls_obj):
            return cls_obj.no_inst
     
    ik1 = Kls()
    ik2 = Kls()
     
    print ik1.get_no_of_instance()
    print Kls.get_no_of_instance()


### Output

    2
    2


The benefit of this is: whether we call the method from the instance or the class, it passes the class as first argument.



##The Python @staticmethod


    IND = 'ON'
     
    class Kls(object):
        def __init__(self, data):
            self.data = data
     
        @staticmethod
        def checkind():
            return (IND == 'ON')

     
    ik1 = Kls(12)
    ik1.checkind()
    Kls.checkind()


You can also call class_foo using the class. In fact, if you define something to be a classmethod, it is probably because you intend to call it from the class rather than from a class instance. 

With staticmethods, neither self (the object instance) nor cls (the class) is implicitly passed as the first argument. 
They behave like plain functions except that you can call them from an instance or the class.










