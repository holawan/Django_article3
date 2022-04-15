from django.shortcuts import get_object_or_404, render, redirect

from movies.forms import MovieForm
from .models import Movie
# Create your views here.


def index(request) :
    movies = Movie.objects.all()

    context = {

        'movies' :movies 
    }

    return render(request,'movies/index.html',context)

def create(request):
    if request.method=='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            movie.save()
            return redirect('movies:index')
    form = MovieForm()
    context = {
        'form' : form
    }
    return render(request,'movies/create.html', context)

def update(request,pk):
    movie = get_object_or_404(Movie, pk=pk)
    # if request.method=='POST':

    #     form = MovieForm(request.POST, instance=movie)
    #     if form.is_valid():
    #         movie = form.save()
    #         movie.save()
    #         return redirect('movies:index')
    form = MovieForm(instance=movie)
    context = {
        'form' : form,
        'movie' : movie
    }
    return render(request,'movies/update.html', context)    



def detail(request,pk) :
    movie = get_object_or_404(Movie,pk=pk) 

    context = {
        'movie' :movie
    }

    return render(request, 'movies/detail.html',context)
