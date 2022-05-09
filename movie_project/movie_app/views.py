from django.shortcuts import render, get_object_or_404
from django.db.models import F

# Create your views here.
from .models import Movie


def show_all_movie(request):
    movies = Movie.objects.order_by(F('year').desc(nulls_last=True), '-rating')

    for movie in movies:
        movie.save()
    return render(request, 'movie_app/all_movies.html', {'movies': movies})

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})