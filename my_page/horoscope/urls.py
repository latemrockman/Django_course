from django.urls import path
from . import views

urlpatterns = [
    path('leo', views.leo),
    path('scorpio', views.scorpio),
]