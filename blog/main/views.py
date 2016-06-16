from django.shortcuts import render

# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from main.models import *
from django.views.generic import ListView


from django.http import HttpResponse, HttpResponseRedirect

from django.conf import settings

def change_language(request):
    _next = request.REQUEST.get('next', None)
    #removing language prefix
    for supported_language in settings.LANGUAGES:
        prefix = '/%s/' % supported_language[0]
        if _next.startswith(prefix):
            _next = _next[len(prefix):]
            break

    language = request.REQUEST.get(u'language', 'en')
    if _next == '/':
        response = HttpResponseRedirect('/')
    else:
        response = HttpResponseRedirect('/%s/%s' % (language, _next))

    return response

from main.form import NameForm

from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required

@cache_page(30)
@login_required
def home_page(request):
    #print request.method
    from main.tasks import save_message, send_message
    #save_message.delay()
    #send_message.delay()
    m = Musician.objects.all()
    message = ''
    if request.method == 'POST':
        
        form = NameForm(request.POST)
           
        if form.is_valid():
            form.save()
            message = 'Well'
            return HttpResponseRedirect('/'+request.LANGUAGE_CODE+'/')
        else:
            message = 'Some error!!!'
    else:        
        form = NameForm()
    #import pdb; pdb.set_trace()
    context = {'name': 'Dima', 'form': NameForm(),'message': message}
    return render_to_response('main/home.html', context, RequestContext(request))


class MusicianListView(ListView):
    model = Musician

