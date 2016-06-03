from django.shortcuts import render

# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from main.models import *
from django.views.generic import ListView


def home_page(request):
    #print request.method
    m = Musician.objects.all()
    #import pdb; pdb.set_trace()
    context = {'name': 'Dima', 'm': m}
    return render_to_response('main/home.html', context, RequestContext(request))


class MusicianListView(ListView):
    model = Musician

