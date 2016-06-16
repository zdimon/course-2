###The contenttypes framework

Django includes a contenttypes application that can track all 
of the models installed in your Django-powered project, providing 
a high-level, generic interface for working with your models

At the heart of the contenttypes application is the ContentType model,
which lives at django.contrib.contenttypes.models.ContentType. 
Instances of ContentType represent and store information about 
the models installed in your project, and new instances of ContentType 
are automatically created whenever new models are installed.

    # ourapp.models
    from django.conf import settings
    from django.db import models

    # Assign the User model in case it has been "swapped"
    User = settings.AUTH_USER_MODEL

    # Create your models here
    class Post(models.Model):
      author = models.ForeignKey(User)
      title = models.CharField(max_length=75)
      slug = models.SlugField(unique=True)
      body = models.TextField(blank=True)

    class Picture(models.Model):
      author = models.ForeignKey(User)
      image = models.ImageField()
      caption = models.TextField(blank=True)

    class Comment(models.Model):
      author = models.ForeignKey(User)
      body = models.TextField(blank=True)
      post = models.ForeignKey(Post)
      picture = models.ForeignKey(Picture)




    from django.contrib.contenttypes import generic
    from django.contrib.contenttypes.models import ContentType

    ...

    class Comment(models.Model):
      author = models.ForeignKey(User)
      body = models.TextField(blank=True)
      content_type = models.ForeignKey(ContentType)
      object_id = models.PositiveIntegerField()
      content_object = generic.GenericForeignKey()
