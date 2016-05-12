class cat(object):
    color = 1
    def say():
        print 'miauuu'


c = cat()

#import pdb; pdb.set_trace()

if hasattr(c, 'say'):
    print 'object %s has attribute say' % c


if hasattr(c, 'color'):
    print 'object %s has attribute color' % c
else:
    print 'object %s has NOT attribute color' % c

m =  getattr(c, "say", None)

if callable(m):
    print 'Say is the function!!!'
    



