from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        'movie': movie
    }
    return render(request, 'detail.html', context)


def form(request):
    return render(request, 'form.html')


def create(request):
    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    open_data = request.GET.get('open_data')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')

    movie = Movie()
    movie.title = title
    movie.title_en = title_en
    movie.audience = audience
    movie.open_data = open_data
    movie.genre = genre
    movie.watch_grade = watch_grade
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()

    return redirect('/movies/')


def edit(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        'movie': movie
    }
    return render(request, 'edit.html', context)


def update(request, id):
    movie = Movie.objects.get(id=id)

    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    open_data = request.GET.get('open_data')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')

    movie.title = title
    movie.title_en = title_en
    movie.audience = audience
    movie.open_data = open_data
    movie.genre = genre
    movie.watch_grade = watch_grade
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()

    return redirect('/movies/')


def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('/movies/')
