"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
urlpatterns = [
#URLS for movies
    #path('GET/movies/', getMovies),
    path('movies/<int:movieId>', getMoviesId),
    path('movies/new', postMovies),
    path('movies/change/<int:movieId>', putMovies),
    path('movies/delete/<int:movieId>', deleteMovies),
    
#URLS for directors
    path('directors/<int:directorId>', getDirectorsId),
    path('directors/new', postDirectors),
    path('directors/delete/<int:directorId>', deleteDirectors),
    path('directors/change/<int:directorId>', putDirectors)
]
