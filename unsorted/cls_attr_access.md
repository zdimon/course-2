##Customizing attribute access

    class Hi(object):
        def __getattr__(self,name):
            print 'do you want %s?' % name
        
