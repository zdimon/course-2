## Link on the item

To create link we need to define special 
function get_absolute_url inside model class.

   def get_absolute_url(self):
        return "/people/%i/" % self.id


    from django.core.urlresolvers import reverse

    def get_absolute_url(self):
        return reverse('people.views.details', args=[str(self.id)])

    ---urls.py---        

    url(r'^people/(?P<id>\d+)$', 'people.views.details'),


Template

    <a href="{{ i.get_absolute_url }}" >Detail</a>
