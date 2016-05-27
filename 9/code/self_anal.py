class mycls(object):
    def hello():
        print 'hello'

obj = mycls

for i in dir(mycls):
    #print "%s::::%s" % (i,mycls.i)
    print "%s::::%s" % (i,getattr(mycls,i))

import pdb; pdb.set_trace()

