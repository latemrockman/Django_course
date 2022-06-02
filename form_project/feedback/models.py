from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=60)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()
