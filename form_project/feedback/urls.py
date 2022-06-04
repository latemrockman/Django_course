from django.contrib import admin
from django.urls import path
from .views import index, done, update_feedback

urlpatterns = [
    path('done', done, name='done'),
    path('', index, name='index'),
    path('<int:id_feedback>', update_feedback, name='update-feedback'),

]