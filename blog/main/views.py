from django.shortcuts import render

# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response



def home_page(request):
    context = {}
    return render_to_response('main/home.html', context, RequestContext(request))
