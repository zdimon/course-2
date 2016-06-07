class Mynumber(object):

    def __init__(self, num, max):
        self.max = max
        self.num = num


    def __get__(self, instance, cls):
        print 'getting number'
        return self.num

    def __set__(self,instance,value):
        print 'trying to set number %s' % value
        if value>instance.maxa:
            raise TypeError("Must be less then %s" % instance.maxa) 
        self.num = value

    def __delete__(self,instance):
        raise AttributeError("Can't delete attribute")

class Account(object):
    number = Mynumber(3,10)
    maxa = 40

aa = Account()

import pdb; pdb.set_trace()


