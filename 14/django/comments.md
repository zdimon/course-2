###Comments

Install

    pip install django-contrib-comments

    'django_comments',


Migration



    urlpatterns = [
        ...
        url(r'^comments/', include('django_comments.urls')),
        ...
    ]

Template tag

    {% load comments %}


    {% render_comment_form for [object] %}

