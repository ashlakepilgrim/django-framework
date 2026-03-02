from django.contrib import admin
from .models import Book, Movie, Anime

# Register your models here.
admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Anime)