#Lambda functions

Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda". 


    def f (x): return x**2

    print f(2)



    ff = lambda x: x**2

    print ff(2)

The following code fragments demonstrate the use of lambda functions.

    def make_incrementor (n): 
        return lambda x: x + n

    d = make_incrementor(20)
    print d
    print d(3)
