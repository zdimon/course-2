"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.flatpages import views
from main.views import home_page, MusicianListView

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    url(r'^$', home_page),
    url(r'^rosetta', include('rosetta.urls')),
    url(r'^change_language/', 'main.views.change_language', name='change_language'),
    url(r'^page/(?P<slug>[^\.]+)', 'page.views.detail', name='show_page'),
     url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
     url(r'^login/$', 'django.contrib.auth.views.login', name='login'),    
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^class$', MusicianListView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^about-us/$', views.flatpage, {'url': '/about/'}, name='about'),
    url(r'^help/$', views.flatpage, {'url': '/help/'}, name='help'),
    url(r'^contact/$', views.flatpage, {'url': '/contact/'}, name='contact'),
    url(r'^accounts/', include('registration.backends.default.urls')),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
