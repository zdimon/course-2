class LessThanZeroException(Exception):
    pass

class variable(object):
    def __init__(self, value=0):
        self.__x = value

    def __set__(self, obj, value):
        print '%s you are traing to set value: %s obj: %s' % (self, value, obj)
        if value < 0:
            raise LessThanZeroException('x is less than zero')

        self.__x  = value

    def __get__(self, obj, objType):
        print '%s you are traing to get  obj: %s objType: %s' % (self, obj,objType)
        return self.__x

class MyClass(object):
    x = variable()

class tt(object):
    pass

m = MyClass()

import pdb; pdb.set_trace()

