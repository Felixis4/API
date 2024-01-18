

from django.urls import path, include
from .views import getMovies,getMoviesId,postMovies,putMovies,deleteMovies
from .views import getDirectorsId,postDirectors,deleteDirectors,putDirectors
from .views import postCountrys, customErrors

urlpatterns = [
#URLS for movies
    path('movies/', getMovies),
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
    path('<path:invalid_path>', customErrors),
]
