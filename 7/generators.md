##Generators iterators

### Iterators


We use for statement for looping over a list.

    for i in [1, 2, 3, 4]:
        print i,

over string

    for c in "python":
        print c

over file

    for line in open("a.txt"):
        print line,





Containers 
Containers are data structures holding elements, and that support membership tests. They are data structures that live in memory, and typically hold all their values in memory, too. 

Most containers are iterable.


>>> x = [1, 2, 3]
>>> y = iter(x)
>>> z = iter(x)
>>> next(y)
1
>>> next(y)
2
>>> next(z)
1
>>> type(x)
<class 'list'>
>>> type(y)
<class 'list_iterator'>



http://nvie.com/posts/iterators-vs-generators/
http://anandology.com/python-practice-book/iterators.html

