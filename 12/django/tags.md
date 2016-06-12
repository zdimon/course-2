##Tags


    pip install django-taggit==0.12.2



    Add "taggit" to your INSTALLED_APPS

    INSTALLED_APPS = (
        'django.contrib.admin',
        [...]
        'taggit',
    )

Run migration

    ./manage.py migrate

Add a TaggableManager to your model and go.

from taggit.managers import TaggableManager

[...]

class Item(models.Model):
    category = models.ForeignKey('Category', verbose_name=u'Категория', null=True, blank=True)
    [...]
    tags = TaggableManager()
  
Show our tags.

    <div class="well">
       {% for tag in item.tags.all %}
          <a href="#">{{ tag }}</a>
       {% endfor %}
    </div>

View for tags.

    def item_list_by_tag(request,tag):
        items = Item.objects.filter(tags__name__in=[tag]).all()
        return render(request, 'item_list_by_tag.html', { 'items': items, 'tag': tag})

Create template for this view blog/templates/item_list_by_tag.html.

    {% extends 'base.html' %}

        {% block header %}
            Home page
        {% endblock %}

        {% block content %}
            <h1>Items by tag "{{ tag }}"</h1>

            {% for i in items %}
                <div class="well"><a href="{{ i.get_absolute_url }}">{{ i.text }}</a></div>
            {% endfor %}

        {% endblock %}

        {% block footer %}
            <h3>This is footer</h3>
        {% endblock %}

Now we should add a routing for this page in urls.py.

    url(r'^item/list/by/tag/(?P<tag>[^\.]+).html', 'blog.views.item_list_by_tag', name="item_list_by_tag"),

Finally let's change the template and add the links.

    <h3>Теги</h3>
     <div class="well">
        {% for tag in item.tags.all %}
           <a href="{% url 'item_list_by_tag' tag=tag %}">{{ tag }}</a>
        {% endfor %}
     </div>

