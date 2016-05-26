##Decorator with pars

We have a function which return some price of the good by it's name.
We need to deduct some money from the price without changing code inside target function.

    def set_discount(func):
       def func_wrapper(name):
           return func(name)-2
       return func_wrapper


    @set_discount
    def get_price(name):
        if name == 'apple':
            return 10
        elif name=='banana':
            return 20
        else:
            return 0   


How to pass parameter into @set_discount like this @set_discount(2)


    def set_discount_par(discount):
        def real_decorator(func):
            def func_wrapper(name):
                return func(name)-discount
            return func_wrapper  
        return real_decorator



    @set_discount_par(2)
    def get_price(name):
        if name == 'apple':
            return 10
        elif name=='banana':
            return 20
        else:
            return 0
     
