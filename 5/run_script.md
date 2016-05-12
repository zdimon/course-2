
##Path to the interpreter.

    #!/usr/bin/env python

If you see the error “: No such file or directory” (with nothing before the colon), 
it means that your shebang line has a carriage return at the end, 
presumably because it was edited under Windows (which uses CR,LF as a line separator).

To remove the Windows line endings, you can use. 


    sed -i -e 's/\r$//' filename

--------------tt.py---------------------
                       
    #!/usr/bin/env python


    def myfunc():
        print __name__
        print 'hello'


    if __name__ == '__main__':
        myfunc()

-----------------------------------

    root@python:~/7# ./tt.py
    __main__
    hello

--------im.py----------------------
    from tt import myfunc
    myfunc()

    >> tt
-----------------------------------





