###Ternary Operators

Ternary operators are shortcut for an if-else statement, and are also known as a conditional operators. Here are some examples which you can use to make your code compact and more beautiful.

###[on_true] if [expression] else [on_false]

    x, y = 50, 25
    small = x if x < y else y


###(falseValue, trueValue)[test]

test needs to return True or False.


or you can use the built-in bool() to assure a Boolean value:

###(falseValue, trueValue)[bool(<expression>)]


