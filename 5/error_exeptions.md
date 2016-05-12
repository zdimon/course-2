
###Syntax errors

Syntax errors, also known as parsing errors


>>> while True print 'Hello world'
  File "<stdin>", line 1, in ?
    while True print 'Hello world'
                   ^
SyntaxError: invalid syntax

he parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected. In this example, the error is detected at the keyword print, since a colon (':') is missing before it.

### Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions.

print 10 * (1/0)

ZeroDivisionError: integer division or modulo by zero


while True:
    x = input('first number: ')
    y = input('second number: ')
    try:
        print 'is: %s' % str(x/y)
    except:
        print 'Someting went wrong!'

TypeError: unsupported operand type(s) for /: 'str' and 'int'


first number: 6
second number: 2
is: 3
first number: 6
second number: 0
Someting went wrong!

    try:
        print 'is: %s' % x/y
    except TypeError:
        print 'TypeError exception!'
    except ZeroDivisionError:
        print 'ZeroDivisionError exception!'

A finally clause is always executed before leaving the try statement, whether an exception has occurred or not.


    class AddMoneyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr('User can not add more than %s' % self.value)



    class User(object):
        account = 0
        def add(self,amount):
            if amount>1000:
                raise AddMoneyError(1000)
            else:
                self.account = self.account+amount


    user = User()
    user.add(10000)
    print 'finish operation'


    Traceback (most recent call last):
      File "limit_account.py", line 19, in <module>
        user.add(10000)
      File "limit_account.py", line 13, in add
        raise AddMoneyError(1000)
    __main__.AddMoneyError: 'User can not add more than 1000'


    user = User()
    try:
        user.add(10000)
    except AddMoneyError as e:
        print e    


    zdimon@dell:~/www/lyceum/8/code$ python limit_account.py
    'User can not add more than 1000'
    finish operation
    zdimon@dell:~/www/lyceum/8/code$










