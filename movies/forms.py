from dataclasses import fields
from socket import fromshare
from django import forms
from movies.models import Movie

class MovieForm(forms.ModelForm):

    class Meta: 
        
        model = Movie
        exclude = ('user',)
