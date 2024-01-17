
from django.contrib import admin
from django.urls import path
#from .views import getMovies
from .views import getMoviesId
from .views import postMovies
from .views import putMovies
from .views import deleteMovies
from .views import getDirectorsId
from .views import postDirectors
from .views import deleteDirectors
from .views import putDirectors
from .views import postCountrys

urlpatterns = [
#URLS for movies
    # path('movies/', getMovies),
    path('movies/<int:movieId>', getMoviesId),
    path('movies/new', postMovies),
    path('movies/change/<int:movieId>', putMovies),
    path('movies/delete/<int:movieId>', deleteMovies),
    
#URLS for directors
    path('directors/<int:directorId>', getDirectorsId),
    path('directors/new', postDirectors),
    path('directors/delete/<int:directorId>', deleteDirectors),
    path('directors/change/<int:directorId>', putDirectors),
#-
    path('country/new', postCountrys),
]
