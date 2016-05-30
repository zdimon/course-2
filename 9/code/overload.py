

from datetime import datetime
startTime = datetime.now()

def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)


import pdb; pdb.set_trace()

for index, fibonacci_number in enumerate(fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
     #import pdb; pdb.set_trace()
     if index == 5000:
         break


print datetime.now() - startTime


