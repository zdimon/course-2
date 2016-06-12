##__getattribute__

class M(object):
    var = 12
    def f(self):
        pass
    def __getattribute__(self, attr_name):
        print 'You want to get this %s? OK man' % attr_name
        #return self.attr_name
        #return super(M, self).__getattribute__(attr_name)
s = M()
print s.var
s.f() 
