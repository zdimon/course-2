###Custom admin view

Add new link to list_display array.

    list_display =  (....., 'get_link')

Define function inside class

    def get_link(self, obj):
        from django.utils.safestring import mark_safe
        return mark_safe(u'<a href="'+reverse('admin:do_something', kwargs={'hash': obj.pk})+u'">Do somethig</a>')

Add url. Rewrite get_urls method.

    def get_urls(self):
         from django.conf.urls import patterns, url
         urls = super(MyModelAdmin, self).get_urls()
         my_urls = patterns('',
                            url(r'^do_something/(?P<hash>\w+)',
                                self.admin_site.admin_view(self.do_something),
                                name="do_something")
                            )
        return my_urls + urls

Define function.

    def do_something(self, request, hash):
        from django.http import HttpResponseRedirect
        from django.contrib.auth import authenticate, login, logout
        from django.contrib.auth.models import User
        new_user = User.objects.all().get(id=hash)
        new_user.backend = 'django.contrib.auth.backends.ModelBackend'
        logout(request)
        login(request, new_user)
        return HttpResponseRedirect('/admin')    

