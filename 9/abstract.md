##Abstract methods



    from abc import ABCMeta, abstractmethod

    class Animal:
        __metaclass__ = ABCMeta

        @abstractmethod
        def say_something(self): pass

    class Cat(Animal):
        def say_something(self):
            return "Miauuu!"



A metaclass is the class of a class. 
Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. 
A class is an instance of a metaclass.


