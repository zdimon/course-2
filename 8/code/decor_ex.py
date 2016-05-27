
def set_discount(func):
   def func_wrapper(name):
       return func(name)-2
   return func_wrapper

def set_discount_par(discount):
    def real_decorator(func):
        def func_wrapper(name):
            return func(name)-discount
        return func_wrapper  
    return real_decorator


@set_discount
@set_discount_par(10)
def get_price(name):
    if name == 'apple':
        return 10
    elif name=='banana':
        return 20
    else:
        return 0

price = get_price('banana')
print price





