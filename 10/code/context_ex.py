class cm:
    def __init__(self):
        print '__init__ is called!'
        self.name = 'Dima'
        #print 7/0

    def __enter__(self):
        print '__enter__ is fired!'
        return self.name

    def __exit__(self, type, value, traceback):
        print '__exit__ is executed!'



with cm() as name:
     #print 7/0
     print 'name is %s' % name
