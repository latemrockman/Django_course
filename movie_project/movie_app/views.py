from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value

# Create your views here.
from .models import Movie


def show_all_movie(request):
    #movies = Movie.objects.order_by(F('year').desc(nulls_last=True), '-rating')

    movies = Movie.objects.annotate(
        privet_true=Value(True),
        privet_false=Value(False),
        privet_str=Value('hello'),
        privet_int=Value(123),
        new_budget=F('budget') + 555,
        new_rating=F('rating') * F('year')
    )

    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('name'))

    for movie in movies:
        movie.save()
    return render(request, 'movie_app/all_movies.html',
                  {'movies': movies,
                   'agg': agg,
                   'total': movies.count(),                         # кол-во записей можно еще так получить
                   'midl': movies.aggregate(Avg('budget'))          # среднее кол-во так
                   })

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})