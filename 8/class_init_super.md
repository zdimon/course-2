###Class

The simplest form of class definition looks like this:

    class ClassName(object):
        <statement-1>
        .
        .
        .
        <statement-N>


    class MyClass(object):
        """A simple example class"""
        i = 12345
        def f(self):
            return 'hello world'


    x = MyClass()

The instantiation operation (“calling” a class object) creates an empty object.
Many classes like to create objects with instances customized to a specific initial state. 
Therefore a class may define a special method named __init__(), like this:

    def __init__(self):
        self.i = 54321




    class Car(object):

        def __init__(self):
            self.doors = 2

        def move(self):
            return 'dr-dr-dr-d'


    c = Car()
    print c.doors


    class Lorry(Car):

        def __init__(self):
            self.color = 'red'


    l = Lorry()
    print l.color
    print l.doors

We will get error.


    AttributeError: 'Lorry' object has no attribute 'doors'


    def __init__(self):
        self.color = 'red'
        super(Lorry, self).__init__() # we need to call Car.__init__() func



    
