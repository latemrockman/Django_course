from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie, name='movie-index'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name="movie-details"),
    path('actor/', views.show_all_actors, name='all-actors'),
    path('actor/<slug:slug_actor>', views.show_one_actor, name='actor-details'),
    path('director/', views.show_all_directors, name='all-directors'),
    #path('director/<int:id_director>', views.show_one_director, name='director-details'),
    path('director/<slug:slug_director>', views.show_one_director, name='director-details')
]