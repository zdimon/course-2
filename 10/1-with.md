##With

Consider this piece of code:

    set things up
    try:
        do something
    finally:
        tear things down


If you do this a lot, it would be quite convenient if 
you could put the “set things up” and “tear things down” 
code in a library function, to make it easy to reuse.


    def controlled_execution(callback):
        set things up
        try:
            callback(thing)
        finally:
            tear things down

    def my_function(thing):
        do something

    controlled_execution(my_function)



python-dev team finally came up with a generalization 
of the latter, using an object instead of function



    class controlled_execution:
        def __enter__(self):
            set things up
            return thing
        def __exit__(self, type, value, traceback):
            tear things down

    with controlled_execution() as thing:
         some code

    

Now, when the “with” statement is executed, 
Python evaluates the expression, calls the __enter__ 
method on the resulting value 
(which is called a “context guard”), 
and assigns whatever __enter__ returns 
to the variable given by as. 
Python will then execute the code body, 
and no matter what happens in that code, 
call the guard object’s __exit__ method. 

As an extra bonus, the __exit__ 
method can look at the exception

    def __exit__(self, type, value, traceback):
        return isinstance(value, TypeError)


so to open a file, process its contents, 
and make sure to close it, you can simply do:

    with open("x.txt") as f:
        data = f.read()
        do something with data



