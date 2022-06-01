from django.contrib import admin
from django.urls import path
from .views import index, done

urlpatterns = [
    path('done', done, name='done'),
    path('', index, name='index'),
]