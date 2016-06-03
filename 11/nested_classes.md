##Nested classes

http://www.brpreiss.com/books/opus7/html/page598.html

###Logical grouping of classes: 

If a class is useful to only one other class then it is logical 
to embed it in that class and keep the two together. 
Nesting such "helper classes" makes their package more streamlined.




###Increased encapsulation: 

Consider two top-level classes A and B where 
B needs access to members of A that would 
otherwise be declared private. 
By hiding class B within class A A's members 
can be declared private and B can access them. 
In addition B itself can be hidden from the outside world.


###More readable, maintainable code: 

Nesting small classes within top-level 
classes places the code closer to where it is used.


    def foo():
        class bar(object):
            ...
        z = bar()


