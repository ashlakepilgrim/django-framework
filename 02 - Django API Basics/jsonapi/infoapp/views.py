from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Book, Movie, Anime

# Create your views here.
def index(request):
    # pass
    data = {
        "message": "Welcome to Info API.",
        "categories": [
            "books",
            "movies",
            "animes"
        ]
    }
    return JsonResponse(data)

# def books(request):
#     # pass
#     books = Book.objects.all()
#     data = [
#         {
#             "id": b.id,
#             "title": b.title,
#             "author": b.author,
#             "genre": b.genre,
#             "published_year": b.published_year,
#             "rating": b.rating,
#             "available": b.available
#         }
#         for b in books
#     ]
#     return JsonResponse(data, safe=False)

def books(request):

    try:
        # If no query params, fetch all books and return them
        books = Book.objects.all()

        # If query params, extract them and then proceed
        available = request.GET.get("available")
        order = request.GET.get("order")
        rating = request.GET.get("rating")

        if available is not None:
            if available.lower() == "true":
                # books = Book.objects.filter(available=True)
                # if multiple filters are there then it's better to filter from existing queryset
                books = books.filter(available=True)
            elif available.lower() == "false":
                books = books.filter(available=False)
            else:
                return JsonResponse({
                    "status": 400,
                    "error": 'query param available value must be either true or false'
                }, status=400)
        
        if order is not None:
            if order.lower() == "asc":
                books = books.order_by("title")
            elif order.lower() == "desc":
                books = books.order_by("-title")
            else:
                return JsonResponse({
                    "status": 400,
                    "error": 'query param order value must be either asc or desc'
                }, status=400)
            
        if rating is not None:
            try:
                clean_rating = float(rating)

                if not (0 <= clean_rating <= 5):
                    return JsonResponse({
                        "status": 400,
                        "error": 'rating must be between 0 and 5'
                    }, status=400)
                
                # __gte is a field lookup that stands for greater than or equal to
                books = books.filter(rating__gte=clean_rating)
            except ValueError:
                return JsonResponse({
                    "status": 400,
                    "error": "rating must be a number"
                }, status=400)

        data = [
            {
                "id": b.id,
                "title": b.title,
                "author": b.author,
                "genre": b.genre,
                "published_year": b.published_year,
                "rating": b.rating,
                "available": b.available
            }
            for b in books
        ]

        response = {
            "status": 200,
            "data": data
        }

        return JsonResponse(response, status=200)
    
    except Exception as e:

        return JsonResponse({
            "status": 500,
            "error": str(e)
        }, status=500)

def movies(request):
    # pass
    movies = Movie.objects.all()
    data = [
        {
            "id": m.id,
            "title": m.title,
            "director": m.director,
            "genre": m.genre,
            "release_year": m.release_year,
            "rating": m.rating,
            "available": m.available
        }
        for m in movies
    ]
    return JsonResponse(data, safe=False)

def animes(request):
    # pass
    animes = Anime.objects.all()
    data = [
        {
            "id": a.id,
            "title": a.title,
            "studio": a.studio,
            "genre": a.genre,
            "release_year": a.release_year,
            "rating": a.rating,
            "episodes": a.episodes,
            "completed": a.completed
        }
        for a in animes
    ]
    return JsonResponse(data, safe=False)

def book_details(request, id):
    # pass
    book = get_object_or_404(Book, pk=id)
    data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "published_year": book.published_year,
        "rating": book.rating,
        "available": book.available
    }
    return JsonResponse(data)

def movie_details(request, id):
    # pass
    movie = get_object_or_404(Movie, pk=id)
    data = {
        "id": movie.id,
        "title": movie.title,
        "director": movie.director,
        "genre": movie.genre,
        "release_year": movie.release_year,
        "rating": movie.rating,
        "available": movie.available
    }
    return JsonResponse(data)

def anime_details(request, id):
    # pass
    anime = get_object_or_404(Anime, pk=id)
    data = {
        "id": anime.id,
        "title": anime.title,
        "studio": anime.studio,
        "genre": anime.genre,
        "release_year": anime.release_year,
        "rating": anime.rating,
        "episodes": anime.episodes,
        "completed": anime.completed
    }
    return JsonResponse(data)

# OLD VIEWS

# def books(request):
#     # pass
#     data = {
#         "message": "Info API - Books",
#         "books": {
#             "1": {
#                 "id": 1,
#                 "title": "The Hobbit",
#                 "author": "J.R.R. Tolkien",
#                 "genre": "Fantasy",
#                 "publishedYear": 1937,
#                 "rating": 4.8,
#                 "available": True
#             },
#             "2": {
#                 "id": 2,
#                 "title": "1984",
#                 "author": "George Orwell",
#                 "genre": "Dystopian",
#                 "publishedYear": 1949,
#                 "rating": 4.7,
#                 "available": False
#             },
#             "3": {
#                 "id": 3,
#                 "title": "To Kill a Mockingbird",
#                 "author": "Harper Lee",
#                 "genre": "Classic",
#                 "publishedYear": 1960,
#                 "rating": 4.9,
#                 "available": True
#             },
#             "4": {
#                 "id": 4,
#                 "title": "The Great Gatsby",
#                 "author": "F. Scott Fitzgerald",
#                 "genre": "Classic",
#                 "publishedYear": 1925,
#                 "rating": 4.6,
#                 "available": True
#             },
#             "5": {
#                 "id": 5,
#                 "title": "Atomic Habits",
#                 "author": "James Clear",
#                 "genre": "Self-Help",
#                 "publishedYear": 2018,
#                 "rating": 4.8,
#                 "available": True
#             }
#         }
#     }
#     return JsonResponse(data)

# def movies(request):
#     # pass
#     data = {
#         "message": "Info API - Movies",
#         "movies": {
#             "1": {
#                 "id": 1,
#                 "title": "The Dark Knight",
#                 "director": "Christopher Nolan",
#                 "genre": "Action",
#                 "releaseYear": 2008,
#                 "rating": 4.9,
#                 "available": True
#             },
#             "2": {
#                 "id": 2,
#                 "title": "Inception",
#                 "director": "Christopher Nolan",
#                 "genre": "Sci-Fi",
#                 "releaseYear": 2010,
#                 "rating": 4.8,
#                 "available": False
#             },
#             "3": {
#                 "id": 3,
#                 "title": "Parasite",
#                 "director": "Bong Joon-ho",
#                 "genre": "Thriller",
#                 "releaseYear": 2019,
#                 "rating": 4.7,
#                 "available": True
#             },
#             "4": {
#                 "id": 4,
#                 "title": "Interstellar",
#                 "director": "Christopher Nolan",
#                 "genre": "Sci-Fi",
#                 "releaseYear": 2014,
#                 "rating": 4.8,
#                 "available": True
#             },
#             "5": {
#                 "id": 5,
#                 "title": "The Shawshank Redemption",
#                 "director": "Frank Darabont",
#                 "genre": "Drama",
#                 "releaseYear": 1994,
#                 "rating": 4.9,
#                 "available": True
#             }
#         },
#     }
#     return JsonResponse(data)

# def animes(request):
    # pass
    data = {
        "message": "Info API - Animes",
        "animes": {
            "1": {
                "id": 1,
                "title": "Attack on Titan",
                "studio": "MAPPA",
                "genre": "Action",
                "releaseYear": 2013,
                "rating": 4.9,
                "episodes": 87,
                "completed": True
            },
            "2": {
                "id": 2,
                "title": "Naruto",
                "studio": "Pierrot",
                "genre": "Adventure",
                "releaseYear": 2002,
                "rating": 4.7,
                "episodes": 220,
                "completed": True
            },
            "3": {
                "id": 3,
                "title": "Demon Slayer",
                "studio": "Ufotable",
                "genre": "Fantasy",
                "releaseYear": 2019,
                "rating": 4.8,
                "episodes": 55,
                "completed": False
            },
            "4": {
                "id": 4,
                "title": "One Piece",
                "studio": "Toei Animation",
                "genre": "Adventure",
                "releaseYear": 1999,
                "rating": 4.8,
                "episodes": 1000,
                "completed": False
            },
            "5": {
                "id": 5,
                "title": "Death Note",
                "studio": "Madhouse",
                "genre": "Thriller",
                "releaseYear": 2006,
                "rating": 4.9,
                "episodes": 37,
                "completed": True
            }
        }
    }
    return JsonResponse(data)