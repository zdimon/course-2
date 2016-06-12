##Class decorator

    def method_decorator(fn):
        "Example of a method decorator"
        def decorator(*args, **kwargs):
            print "\tInside the decorator"
            return fn(*args, **kwargs)

        return decorator

    class MyFirstClass(object):
        """
        This class has all its methods decorated
        """
        @method_decorator
        def first_method(self, *args, **kwargs):
            print "\t\tthis is a the MyFirstClass.first_method"

        @method_decorator
        def second_method(self, *args, **kwargs):
            print "\t\tthis is the MyFirstClass.second_method"

    if __name__ == "__main__":
        print "::: With decorated methods :::"
        x = MyFirstClass()
        x.first_method()
        x.second_method()



The problem is that every time you want this behaviour 
in a certain class method you have to decorate it. 

The other solution its to write a class decorator, 
where you select which methods to decorate passing 
their names as the decorator arguments.

    @class_decorator('first_method', 'second_method')
    class MySecondClass(object):



    def method_decorator(fn):
        "Example of a method decorator"
        def decorator(*args, **kwargs):
            print "\tInside the decorator"
            return fn(*args, **kwargs)

        return decorator


    def class_decorator(*method_names):
        def class_rebuilder(cls):
            "The class decorator example"
            class NewClass(cls):
                "This is the overwritten class"
                def __getattribute__(self, attr_name):
                    obj = super(NewClass, self).__getattribute__(attr_name)
                    if hasattr(obj, '__call__') and attr_name in method_names:
                        return method_decorator(obj)
                    return obj

            return NewClass
        return class_rebuilder


    @class_decorator('first_method', 'second_method')
    class MySecondClass(object):
        """
        This class is decorated
        """
        def first_method(self, *args, **kwargs):
            print "\t\tthis is a the MySecondClass.first_method"

        def second_method(self, *args, **kwargs):
            print "\t\tthis is the MySecondClass.second_method"

    if __name__ == "__main__":
        print "::: With a decorated class :::"
        z = MySecondClass()
        z.first_method()
        z.second_method()



