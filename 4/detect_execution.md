##Define execution

When we import some module the code inside this module will be executed. 
When the Python interpreter reads a source file, it executes all of the code found in it. 
Before executing the code, it will define a few special variables. 
For example, if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.

    #!/usr/bin/env python
    print 'hi'

    def myfunc():
        print 'hello'



    from mymodule import myfunc

    >> hi

__name__ - special variable inside each module.


    if __name__ == "__main__":
        print("one.py is being run directly")
    else:
        print("one.py is being imported into another module")
