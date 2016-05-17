from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hobby(models.Model):
    name = models.CharField(max_length=50)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    hobby = models.ManyToManyField(Hobby)
    def __unicode__(self):
        return '%s %s (%s)' % (self.first_name, self.last_name, self.instrument)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Supermusician(Musician):
    supername = models.CharField(max_length=100)









