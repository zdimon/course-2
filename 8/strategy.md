## Pattern strategy

    class animal(object):

        sound = 'uuuuuuuuuuuuu!'
        def say(self):
            print self.sound

        def move(self):
            print 'I go a head!'

        def display(self):
            print '''##########DISPLAY########'''


    class cat(animal):
        pass


    class animal(object):

        sound = 'uuuuuuuuuuuuu!'
        def say(self):
            print self.sound

        def move(self):
            print 'I go a head!'

        def display(self):
            print '''##########DISPLAY########'''

        def fly(self):
            print 'I can fly'

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






    class canfly():
        def fly(self):
            print 'I can fly'   

    class cannotfly():
        def fly(self):
            print 'I can NOT fly' 



    class animal(object):
        sound = 'uuuuuuuuuuuuu!'
        fly_behavior = None
        def say(self):
            print self.sound

        def move(self):
            print 'I go a head!'
        
        def display(self):
            print '''##########DISPLAY########'''  


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

