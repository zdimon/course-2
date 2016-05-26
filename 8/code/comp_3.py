
class Messanger(object):

    def __init__(self,message,sender):
        self.message = message
        self.sender = sender

    def send(self):
        self.sender.send(self.message)


class EmailSender():

    def send(self,message):
        print 'I am sending this %s via email' % message
        
class SkypeSender():

    def send(self,message):
        print 'I am sending this %s via skype' % message

class SmsSender():

    def send(self,message):
        print 'I am sending this %s via sms' % message

email_sender = EmailSender()
message = Messanger('hello',email_sender)
message.send()


email_sender = EmailSender()
message = Messanger('hello',email_sender)
message.send()
message.sender = SmsSender()
message.send()




