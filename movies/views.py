import json
from django.http import JsonResponse
#from rest_framework.decorators import   
from django.views.decorators.csrf import csrf_exempt
from .models import Movies
from django.shortcuts import get_object_or_404
from django.db import models




#@api_view(['GET', 'POST', 'DELETE' , 'PUT',])


# @csrf_exempt
# def getMovies(request):
#         allmovies=Movies.objects.all()
#         getthatfuckinmovies=[allmovies.title for movie in allmovies]
        
#         return JsonResponse({getthatfuckinmovies})
        


@csrf_exempt  
def getMoviesId(request, movieId):
        
    movie = get_object_or_404(Movies, id=movieId)
        
    movieName = movie.title

    return JsonResponse({
            'movie': movieName,
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
        
        
        return JsonResponse({'status': 'success', 'message': 'Movie Added'})

    else:
        
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
    
    
    
# @csrf_exempt
# def deleteMovies(request):
#     if request.method=='DELETE':
    
#         data = json.loads(request.body)

            
#         key_to_delete = data.get('key', '')

#         if key_to_delete in movies_array:
#             del movies_array[key_to_delete]
#             return JsonResponse({'message': f'movie number "{key_to_delete}" deleted successfully!'})
#     else:
#         return JsonResponse({'error': f'movie number "{key_to_delete}" not found'}, status=404)