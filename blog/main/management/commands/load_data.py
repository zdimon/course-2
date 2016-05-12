from django.core.management.base import BaseCommand, CommandError
from main.models import *
from mixer.backend.django import mixer

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'




    def handle(self, *args, **options):
        #client = mixer.cycle(10000).blend(Musician)
        m = Musician(first_name='tester')
        m.save()
        a = Album()
        a.artist = m
        a.release_date='2016-10-10'
        a.num_stars = 23
        a.save()
        print help
