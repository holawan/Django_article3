from dataclasses import fields
from socket import fromshare
from django import forms
from movies.models import Movie,Comment

class MovieForm(forms.ModelForm):

    class Meta: 
        
        model = Movie
        exclude = ('user',)
class CommentForm(forms.ModelForm) :

    class Meta :

        model = Comment
        fields = ('content',)