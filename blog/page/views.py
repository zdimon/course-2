from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from page.models import *
# Create your views here.

def detail(request,slug):
    page = get_object_or_404(Page, slug=slug)
    return render_to_response('page/detail.html', {'page': page}, RequestContext(request))
