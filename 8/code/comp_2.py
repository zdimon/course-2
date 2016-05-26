class Messanger(object):
    message = None
    transport = 'email'
    def check_on_stop_word(self,message):
        if 'fuck' in message.split():
            return '***'
        return message

    def __init__(self,message):
        print message   
        self.message = self.check_on_stop_word(message)

    def send(self):
        if self.transport == 'email':
            print 'send message %s by email' % self.message
        elif self.transport == 'icq':
            print 'send message %s by icq' % self.message
        else:
            print 'send message %s to nowere' % self.message
        





class Email(Messanger):

    def connect():
        print 'Make connection to smtp server'

class Icq(Messanger):

    def connect():
        print 'Make connection to icq server'




m = Email('hello')
m.send()

m = Icq('hello')
m.transport = 'icq'
m.send()

