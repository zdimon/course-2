### *args **kwargs

The names *args and **kwargs are only by convention but there's no hard requirement to use them.

You would use *args when you're not sure how many arguments might be passed to your function.


    >>> def print_everything(*args):
            for count, thing in enumerate(args):
    ...         print '{0}. {1}'.format(count, thing)
    ...
    >>> print_everything('apple', 'banana', 'cabbage')
    0. apple
    1. banana
    2. cabbage

Similarly, **kwargs allows you to handle named arguments that you have not defined in advance


    >>> def table_things(**kwargs):
    ...     for name, value in kwargs.items():
    ...         print '{0} = {1}'.format(name, value)
    ...
    >>> table_things(apple = 'fruit', cabbage = 'vegetable')
    cabbage = vegetable
    apple = fruit

