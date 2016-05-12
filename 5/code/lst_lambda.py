items = [1, 2, 3]
lm = lambda x: x**2
l = map(lm, items)
print l

l = map(lambda x: x**2, items)
print l


def square(x): return (x**2)
def cube(x): return (x**3)

funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print value


