
def f():
    global s
    print s
    s = "Hi"
    print s 


s = "Python is great!" 
f()
print s



