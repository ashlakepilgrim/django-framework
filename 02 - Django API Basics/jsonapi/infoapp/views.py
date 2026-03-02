from django.shortcuts import render
from django.http import JsonResponse

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


def books(request):
    # pass
    data = {
        "message": "Info API - Books",
        "books": {
            "1": {
                "id": 1,
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "genre": "Fantasy",
                "publishedYear": 1937,
                "rating": 4.8,
                "available": True
            },
            "2": {
                "id": 2,
                "title": "1984",
                "author": "George Orwell",
                "genre": "Dystopian",
                "publishedYear": 1949,
                "rating": 4.7,
                "available": False
            },
            "3": {
                "id": 3,
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "genre": "Classic",
                "publishedYear": 1960,
                "rating": 4.9,
                "available": True
            },
            "4": {
                "id": 4,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "genre": "Classic",
                "publishedYear": 1925,
                "rating": 4.6,
                "available": True
            },
            "5": {
                "id": 5,
                "title": "Atomic Habits",
                "author": "James Clear",
                "genre": "Self-Help",
                "publishedYear": 2018,
                "rating": 4.8,
                "available": True
            }
        }
    }
    return JsonResponse(data)

def movies(request):
    # pass
    data = {
        "message": "Info API - Movies",
        "movies": {
            "1": {
                "id": 1,
                "title": "The Dark Knight",
                "director": "Christopher Nolan",
                "genre": "Action",
                "releaseYear": 2008,
                "rating": 4.9,
                "available": True
            },
            "2": {
                "id": 2,
                "title": "Inception",
                "director": "Christopher Nolan",
                "genre": "Sci-Fi",
                "releaseYear": 2010,
                "rating": 4.8,
                "available": False
            },
            "3": {
                "id": 3,
                "title": "Parasite",
                "director": "Bong Joon-ho",
                "genre": "Thriller",
                "releaseYear": 2019,
                "rating": 4.7,
                "available": True
            },
            "4": {
                "id": 4,
                "title": "Interstellar",
                "director": "Christopher Nolan",
                "genre": "Sci-Fi",
                "releaseYear": 2014,
                "rating": 4.8,
                "available": True
            },
            "5": {
                "id": 5,
                "title": "The Shawshank Redemption",
                "director": "Frank Darabont",
                "genre": "Drama",
                "releaseYear": 1994,
                "rating": 4.9,
                "available": True
            }
        },
    }
    return JsonResponse(data)

def animes(request):
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