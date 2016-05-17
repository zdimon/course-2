import os

print 'my file is %s' % __file__

print 'absolute path %s' % os.path.abspath(__file__)

print os.path.dirname(os.path.abspath(__file__))

print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
