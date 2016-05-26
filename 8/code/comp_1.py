class Messanger(object):
    message = None

    def check_on_stop_word(self,message):
        if 'fuck' in message.split():
            return '***'
        return message

    def __init__(self,message):
        print message   
        self.message = self.check_on_stop_word(message)




class Email(Messanger):

    def send(self):
        print 'send message %s by email' % self.message


m = Email('do not fuck me')
m.send()
