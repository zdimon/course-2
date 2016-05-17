###subprocess — Subprocess management



The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions:

    os.system
    os.spawn*
    os.popen*
    popen2.*
    commands.*

he recommended way to launch subprocesses is to use the following convenience functions. 

    subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

    subprocess.call(['ls','l'],shell=True)

    subprocess.call(['pwd'],shell=True)

shell=False disables all shell based features, but does not suffer from this vulnerability


    from subprocess import call
    filename = input("What file would you like to display?\n")
    What file would you like to display?
    on_existent; rm -rf / #
    call("cat " + filename, shell=True) # Uh-oh. This will end badly...

###subprocess.check_output

    c = subprocess.check_output(['pwd'],shell=True)

Run command with arguments and return its output as a byte string.


###Popen Constructor

    >>>p = args = ['ls']
    >>> p = subprocess.Popen(args)
    >>> chdir_ex.py  os_ex.py  out_in_file.py  output.txt
    p
    <subprocess.Popen object at 0x7f5248d8f290>

Execute a child program in a new process.


__subprocess.Popen__ is more general than subprocess.call.

Popen doesn't block, allowing you to interact with the process while it's running, or continue with other things in your Python program. The call to Popen returns a Popen object.

Call does block. While it supports all the same arguments as the Popen constructor, so you can still set the process' output, environmental variables, etc., your script waits for the program to complete, and call returns a code representing the process' exit status.


### Redirect output into file

    from subprocess import call
    file = open('output.txt','w')
    call('ls',stdout=file,shell=True)
    print 'done!'


