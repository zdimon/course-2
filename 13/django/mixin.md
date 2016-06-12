##Mixin

Restricting views to non authenticated users. 
With functional views, the code looks something like this:

    from django.contrib.auth.decorators import login_required
    @login_required
    def secret_view(request, *args, **kwargs):
        return HttpResponse('The answer is 42')


However, with class-based views, you're forced into writing the following.

    from django.utils.decorators import method_decorator
    class SecretView(View):

        @method_decorator(login_required)
        def dispatch(self, request, *args, **kwargs):
            return super(SecretView, self).dispatch(request, *args, **kwargs)



A method on a class isn’t quite the same as a standalone function, 
so you can’t just apply a function decorator to the method – you need 
to transform it into a method decorator first. The method_decorator 
decorator transforms a function decorator into a method decorator 
so that it can be used on an instance method.


    class LoginRequiredMixin(object):
        """
        View mixin which requires that the user is authenticated.
        """
        @method_decorator(login_required)
        def dispatch(self, request, *args, **kwargs):
            return super(LoginRequiredMixin, self).dispatch(
                self, request, *args, **kwargs)

    
    from django.contrib.auth.mixins import LoginRequiredMixin

    class MyView(LoginRequiredMixin, View):
        login_url = '/login/'
        redirect_field_name = 'redirect_to'
