##Static blocks


Using template blocks.

    .......base.html..........

    <head>

    {% block js %} 
        <script src="{% static "/static/library/jquery/jquery.min.js" %}"></script>
    {% endblock %}

    {% block css %} 
        <link rel="stylesheet" type="text/css" href="{% static "library/bootstrap/dist/css/bootstrap.css" %}">
    {% endblock %}

    </head>


Inharitanse.

    {% block js %} 
        <script src="{% static "/static/js/my.js" %}"></script>
    {% endblock %}


If you want to leave the html from the parent template you need to use {{ block.super }} statment.
    

    {% block js %} 
        {{ block.super }} 
        <script src="{% static "/static/js/my.js" %}"></script>
    {% endblock %}

##Django compressor

https://django-compressor.readthedocs.io/en/latest/quickstart/

###Instalation

    pip install django_compressor

###Configuration

    INSTALLED_APPS = (
        # other apps
        "compressor",
    )


    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        # other finders..
        'compressor.finders.CompressorFinder',
    )

###Usage

    {% load compress %}
        {% compress <js/css> [<file/inline> [block_name]] %}
        <html of inline or linked JS/CSS>
    {% endcompress %}


###Example

    {% load compress %}

    {% compress css %}
        <link rel="stylesheet" href="/static/css/one.css" type="text/css" charset="utf-8">
        <style type="text/css">p { border:5px solid green;}</style>
        <link rel="stylesheet" href="/static/css/two.css" type="text/css" charset="utf-8">
    {% endcompress %}

Which would be rendered something like:

    <link rel="stylesheet" href="/static/CACHE/css/f7c661b7a124.css" type="text/css" charset="utf-8">


    {% load compress %}

    {% compress js inline %}
        <script src="/static/js/one.js" type="text/javascript" charset="utf-8"></script>
        <script type="text/javascript" charset="utf-8">obj.value = "value";</script>
    {% endcompress %}




