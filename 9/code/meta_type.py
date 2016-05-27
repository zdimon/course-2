def make_myklass(**kwattrs):
    return type('MyKlass', (object,), dict(**kwattrs))

mm = make_myklass(i_am='smart',he_is='fool')

import pdb; pdb.set_trace()

x = mm()

import pdb; pdb.set_trace()

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


import pdb; pdb.set_trace()

print "__call__"

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


