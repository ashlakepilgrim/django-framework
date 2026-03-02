from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    # pass
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    published_year = models.DateField()
    rating = models.DecimalField(decimal_places=1, max_digits=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Movie(models.Model):
    # pass
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_year = models.DateField()
    rating = models.DecimalField(decimal_places=1, max_digits=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Anime(models.Model):
    # pass
    title = models.CharField(max_length=255)
    studio = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_year = models.DateField()
    rating = models.DecimalField(decimal_places=1, max_digits=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    episodes = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title