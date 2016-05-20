def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
d = frange(0,4,1)

import pdb; pdb.set_trace()

for n in frange(0, 4, 0.5):
    print(n)
