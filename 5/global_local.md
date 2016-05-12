##Global and local Variables in Functions

Let's have a look at the following function:

    def f(): 
        print s 
    s = "I hate spam"
    f()


The variable s is defined as the string "I hate spam", before we call the function f(). 
The only statement in f() is the "print s" statement. 
As there is no local s, the value from the global s will be used. 
So the output will be the string "I hate spam". 
The question is, what will happen, if we change the value of s inside of the function f()? 
Will it affect the global s as well? We test it in the following piece of code:

    def f(): 
        s = "Me too."
        print s 

    s = "I hate spam." 
    f()
    print s


###The output looks like this:

    Me too.
    I hate spam.


What if we combine the first example with the second one, i.e. first access s and then assigning a value to it? 
It will throw an error, as we can see the the following example:

    def f(): 
	    print s
	    s = "Me too."
	    print s


    s = "I hate spam." 
    f()
    print s


If we execute the previous script, we get the error message:

    UnboundLocalError: local variable 's' referenced before assignment

Python "assumes" that we want a local variable due to the assignment to s inside of f(), so the first print statement throws this error message. 
Any variable which is changed or created inside of a function is local, if it hasn't been declared as a global variable. 
To tell Python, that we want to use the global variable, we have to use the keyword "global", as can be seen in the following example:


    def f():
        global s
        print s
        s = "That's clear."
        print s 


    s = "Python is great!" 
    f()
    print s

Now there is no ambiguity. The output is as follows:

    Python is great!
    That's clear.
    That's clear.

### Note

    print 'Прювет'

    File "gl_ex1.py", line 4
    SyntaxError: Non-ASCII character '\xd0' in file gl_ex1.py on line 4, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

    We need to add follows line

    # -*- coding: utf-8 -*-
    # coding=utf-8

Local variables of functions __can't be accessed from outside__, when the function call has finished:

    def f():
        s = "I am globally not known"
        print s 

    f()
    print s


If you start this script, you get an output with the following error message:
I am globally not known

    Traceback (most recent call last):
      File "global_local3.py", line 6, in <module>
        print s
    NameError: name 's' is not defined



###How do I check if a variable or method exists

To check the existence of a local variable:

    if 'myVar' in locals():
        # myVar exists.


To check the existence of a global variable:

    if 'myVar' in globals():
        # myVar exists.

To check if an object has an attribute:

    if hasattr(obj, 'attr_name'):
        # obj.attr_name exists.

How to get an attribute

    m =  getattr(c, "say", None)

To check on an ability to call.

    m =  getattr(c, "say", None)
    if callable(m):
        print 'Say is the function!!!'


    
    
 

