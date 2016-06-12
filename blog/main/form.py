from django import forms
from main.models import User
from django.forms import ModelForm

class NameForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
