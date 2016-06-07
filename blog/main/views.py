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


def home_page(request):
    #print request.method
    m = Musician.objects.all()
    #import pdb; pdb.set_trace()
    context = {'name': 'Dima', 'm': m}
    return render_to_response('main/home.html', context, RequestContext(request))


class MusicianListView(ListView):
    model = Musician

