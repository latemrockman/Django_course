from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCYL_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles')
    ]


    name = models.CharField(max_length=40)
    rating = models.IntegerField(blank=True, validators=[MinValueValidator(1),
                                                         MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1800),
                                                                  MaxValueValidator(2022)])
    budget = models.IntegerField(default=10000000, blank=True, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, choices=CURRENCYL_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'


# from movie_app.models import Movie