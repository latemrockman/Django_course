from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie, name='movie-index'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name="movie-detail"),
]