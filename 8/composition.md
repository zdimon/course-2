
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

###Default init value

class Messanger(object):

    def __init__(self,message,sender=EmailSender()):


EmailSender must be defined before Messanger class.


    email_sender = EmailSender()
    message = Messanger('hello')
    message.send()
    message.sender = SmsSender()
    message.send()


I am sending this hello via email
I am sending this hello via sms


