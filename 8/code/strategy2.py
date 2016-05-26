#!/usr/bin/env python
# -*- coding: utf-8 -*-

class animal(object):
    sound = 'uuuuuuuuuuuuu!'
    fly_behavior = None
    def say(self):
        print self.sound

    def move(self):
        print 'I go a head!'
    
    def display(self):
        print '''##########DISPLAY########'''


class canfly():
    def fly(self):
        print 'I can fly'   

class cannotfly():
    def fly(self):
        print 'I can NOT fly'   


class bird(animal):
    def __init__(self):
        self.fly_behavior = canfly()        

class cat(animal):
    def __init__(self):
        self.fly_behavior = cannotfly()    

if __name__ == "__main__":
    o1 = bird()
    o1.display()
    o1.say()
    o1.move()
    o1.fly_behavior.fly()
    ###POLYMORPHISM###########
    def myfly():
        print 'sssssssssssssssss'
    o1.fly_behavior.fly = myfly
    o1.fly_behavior.fly()




