import json
from django.http import JsonResponse   
from django.views.decorators.csrf import csrf_exempt
from .models import Movies
from django.shortcuts import get_object_or_404


# @csrf_exempt
# def getMovies(request):
#         allmovies=Movies.objects.all()
#         getthatfuckinmovies=[allmovies.title for movie in allmovies]
        
#         return JsonResponse({getthatfuckinmovies})

@csrf_exempt  
def getMoviesId(request, movieId):
        
    movie = get_object_or_404(Movies, id=movieId)
        
    movieName = movie.title
    movieYear = movie.year
    movieDirector = movie.director
    movieStudio = movie.studio
    

    return JsonResponse({
            'movie': movieName,
            'Year': movieYear,
            'Director': movieDirector,
            'Studio': movieStudio,
    })

@csrf_exempt
def postMovies(request):
    
    if request.method == 'POST':
        
        json_data = json.loads(request.body.decode('utf-8'))

        newMovie = Movies(
            title=json_data.get('title', ''),
            year=json_data.get('year', ''),
            director=json_data.get('director', ''),
            studio=json_data.get('studio', ''),
        )
        newMovie.save()
        
        return JsonResponse({'status': 'success', 'message': 'Movie Added'})

    else:
        
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

@csrf_exempt
def deleteMovies(request, movieId):
    
    if request.method=='DELETE':
        
        movie = get_object_or_404(Movies, id=movieId)

        
        movie.delete()
            
        return JsonResponse({'message': f'movie number "{movieId}" deleted successfully!'})
    
    else:
        return JsonResponse({'error': f'movie number "{movieId}" not fofound'}, status=404)

@csrf_exempt
def putMovies(request, movieId):
    if request.method=='PUT':
        
        json_data = json.loads(request.body.decode('utf-8'))
        movie = get_object_or_404(Movies, id=movieId)

        movie.title = json_data.get('title', '')
        movie.year = json_data.get('year', '')
        movie.director = json_data.get('director', '')
        movie.studio = json_data.get('studio', '')

        
        movie.save()

        return JsonResponse({'status': 'success', 'message': 'Movie Changed'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)    