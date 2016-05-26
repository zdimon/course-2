#!/usr/bin/env python
# -*- coding: utf-8 -*-


class animal(object):

    sound = 'uuuuuuuuuuuuu!'
    def say(self):
        print self.sound

    def move(self):
        print 'I go a head!'

    def fly(self):
        print 'I can fly'

    def display(self):
        print '''##########DISPLAY########'''

class bird(animal):
    def display(self):
        print "-------DISPLAY BIRD--------"
    def fly(self):
        print 'I can fly'        

class cat(animal):
    def fly(self):
        print 'Oups I can not fly!'   

if __name__ == "__main__":
    o1 = cat()
    o1.display()
    o1.say()
    o1.move()
    o1.fly()
