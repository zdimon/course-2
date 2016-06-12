##Authentication system

###Creating User object

    from django.contrib.auth.models import User
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

###Creating superuser

    manage.py createsuperuser

###Changing password

    from django.contrib.auth.models import User
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

Checking authentication

    if request.user.is_authenticated():
        # Do something for authenticated users.
        ...
    else:
        # Do something for anonymous users.

How to log a user and logout

    from django.contrib.auth import authenticate, login

    def my_view(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                ...
        else:
            # Return an 'invalid login' error message.


    from django.contrib.auth import logout

    def logout_view(request):
        logout(request)
        # Redirect to a success page.
            ...

###The login_required decorator

    from django.contrib.auth.decorators import login_required

    @login_required
    def my_view(request):

    
    @login_required(login_url='/accounts/login/')
   



