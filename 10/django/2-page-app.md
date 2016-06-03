## Page application (Django 1.8)

Create app

    ./manage.py startapp page

Add app in INSTALLED_APPS.

    
Create model.

    # -*- coding: utf-8 -*-
    from django.db import models
    from django.utils.translation import ugettext_lazy as _

    class Page(models.Model):
        title = models.CharField(max_length=250, verbose_name=_(u'Title'))
        content = models.TextField(blank=True)
        seo_content = models.TextField(verbose_name=_(u'МЕТА content'))
        seo_title =   models.TextField(verbose_name=_(u'МЕТА title'))
        seo_keywords = models.TextField(verbose_name=_(u'МЕТА keywords'))
        slug = models.CharField(max_length=250, verbose_name=_(u'Slug'),blank=True)
        def __unicode__(self):
            return self.title
        class Meta:
            verbose_name_plural = 'Pages' 
            verbose_name = 'Page'

Create tables


    ./manage.py makemigrations
    ./manage.py migrate

Add admin app in admin.py.

    from page.models import *

    class PageAdmin(admin.ModelAdmin):
        pass

    admin.site.register(Page, PageAdmin)

Install django-ckeditor-updated

    pip install django-ckeditor-updated

        INSTALLED_APPS = [
        ...
        'page',
        'ckeditor'
    ]

    CKEDITOR_UPLOAD_PATH = "uploads/"
    CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

    CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
    'toolbar': 'Basic',
    },
    }

    CKEDITOR_CONFIGS = {
    'default': {
    'toolbar': 'Full',
    'height': 300,
    'width': 300,
    },
    }

Make sure that MEDIA_ROOT and MEDIA_URL are defined

    MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
    MEDIA_URL = '/uploads/'


Add routing

    url(r'^ckeditor/', include('ckeditor.urls')),


Add serving media files by dev server.

    from django.conf.urls.static import static
    from django.conf import settings

    urlpatterns = [
        url(r'^$', home_page),
        ...
        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    


Using
    
    from ckeditor.fields import RichTextField
    class Page(models.Model):
        ...
        content = RichTextField(blank=True)


Add url.

    url(r'^page/(?P<slug>[^\.]+)', 'page.views.detail', name='show_page'),

Create view

    def detail(request,slug):
        context = {}
        try:
            page = Page.objects.get(slug=slug)
            context = {"page":page}
        except:
            pass
        return render_to_response('detail.html', context, RequestContext(request))

Using shortcuts function

    from django.shortcuts import get_object_or_404

    page = get_object_or_404(Page, slug=slug)

To read https://docs.djangoproject.com/en/1.9/topics/http/shortcuts/


    
## Link on the item

To create link we need to define special 
function get_absolute_url inside model class.

   def get_absolute_url(self):
        return "/page/%i/" % self.id


    from django.core.urlresolvers import reverse

    def get_absolute_url(self):
        return reverse('page.views.detail', args=[str(self.id)])

    ---urls.py---        

    url(r'^people/(?P<id>\d+)$', 'people.views.details'),


Template

    <a href="{{ i.get_absolute_url }}" >Detail</a>

    <a href="{% url 'page' slug='about' %}" >About</a>

    <a href="/page/about" >About</a>
    

    





