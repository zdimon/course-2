ff = lambda x: x**2

print ff(2)


ff = lambda x,y: x*y

print ff(2,3)


def make_incrementor (n): 
    return lambda x: x + n

d = make_incrementor(20)
import pdb; pdb.set_trace()
print d
print d(3)


