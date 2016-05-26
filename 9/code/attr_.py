class Hi(object):
    def __getattribute__(self,name):
        print 'do you want %s?' % name
        return object.__getattribute__(self, name)
        #return self.name

t = Hi()

import pdb; pdb.set_trace()
