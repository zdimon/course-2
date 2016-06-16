##Session cookie

    'django.contrib.sessions.middleware.SessionMiddleware'

Using database-backed sessions

If you want to use a database-backed session, 
you need to add 'django.contrib.sessions' 
to your INSTALLED_APPS setting.

Once you have configured your installation, 
run manage.py migrate to install the single 
database table that stores session data.

    request.session

    request.session['my_var'] = 123
    request.session.get('my_var','default')

    response = render_to_response('main/home.html', context, RequestContext(request))
    response.set_cookie('my_name', 'dimitry')


    response.set_cookie(key, value, max_age=max_age, expires=expires)


This simplistic view sets a has_commented variable to True 
after a user posts a comment. 
It doesn’t let a user post a comment more than once:

def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')


###Using sessions out of views

    from django.contrib.sessions.backends.db import SessionStore
    s = SessionStore()
    # stored as seconds since epoch since datetimes are not serializable in JSON.
    s['last_login'] = 1376587691
    s.save()
    s.session_key
    >>>'2b1189a188b44ad18c35e113ac6ceead'

    s = SessionStore(session_key='2b1189a188b44ad18c35e113ac6ceead')
    s['last_login']



    from django.contrib.sessions.models import Session
    s = Session.objects.get(pk='2b1189a188b44ad18c35e113ac6ceead')
    s.expire_date




