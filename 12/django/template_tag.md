##Template tag

Create this directory structure

    cd main
    mkdir templatetags
    cd templatetags
    touch __init__.py


Create file menu.py with:


    from django import template
    from page.models import Page
    register = template.Library()

    @register.inclusion_tag("main/menu.html")
    def menu():
        out = {}
        pages = Page.objects.all()
        out['pages'] = pages
        return out

Create template templates/main/menu.html


    <ul class="nav nav-pills nav-stacked">
        {% for i in pages %}
            <li>{{ i.title }}</li>
        {% endfor %}
    </ul>

Then you can use your template tag this way

    {% load menu %}
     [...]

    {% menu %}


NOTE!!! You need to restart your server before.

