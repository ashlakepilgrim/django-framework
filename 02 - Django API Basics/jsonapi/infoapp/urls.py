from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("books/", views.books, name='books'),
    path("books/<int:id>", views.book_details, name='book_details'),
    path("movies/", views.movies, name='movies'),
    path("movies/<int:id>", views.movie_details, name='movie_details'),
    path('animes/', views.animes, name="animes"),
    path("animes/<int:id>", views.anime_details, name='anime_details'),
]