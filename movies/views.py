from django.shortcuts import get_object_or_404, render, redirect

from movies.forms import MovieForm,CommentForm
from .models import Movie,Comment
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
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie' :movie,
        'comment_form' : comment_form,
        'comments' : comments
    }

    return render(request, 'movies/detail.html',context)


def delete(request,pk) :
    movie = get_object_or_404(Movie,pk=pk)
    movie.delete()
    return redirect('movies:index')


def comments_create(request,pk) :
    movie = get_object_or_404(Movie,pk=pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid() :
        comment = comment_form.save(commit=False) 
        comment.movie = movie
        comment.save()
        return redirect('movies:detail',movie.pk)
    return redirect('movies:index')

def comments_delete(request,movie_pk,comment_pk) :
    comment = get_object_or_404(Comment,pk=comment_pk)

    comment.delete()
    return redirect('movies:detail',movie_pk)
