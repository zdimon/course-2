

class counter(object):
    cnt = 0
    def __init__(self,number):
        self.cnt = number
    
def sum(x,y):
    print x+y

for i in range(10):
    str = 'obj%s = counter(%s)' % (i,i)
    exec(str)

import pdb; pdb.set_trace()
