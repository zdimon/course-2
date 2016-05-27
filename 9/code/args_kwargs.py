def go(name,age):
    print 'name %s age %s' % (name,age)

def go2(*args):
    print 'name %s age %s' % (args[0],args[1])

def go3(*args,**kwargs):
    print 'name %s age %s' % (args[0],args[1])
    print kwargs['wife']
    #print dict(**kwargs)
    #print kwargs


go('dima',39)

import pdb; pdb.set_trace()

go2('dima',39,34,45,67,88)

import pdb; pdb.set_trace()

go3('dima',39,wife='marina')

