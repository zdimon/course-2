
def f():
    myloc = 'hello'
    print globals()
    print locals()
    if 'myloc' in locals():
        print 'myloc is in locals'
    else:
        print 'myloc is NOT in locals'

myglob = 'Dmitry'

print locals()

print globals()

if 'myloc' in globals():
    print 'myloc is in globals'
else:
    print 'myloc is NOT in globals'

if 'myloc' in locals():
    print 'myloc is in locals'
else:
    print 'myloc is NOT in locals'

f()

