import json
from django.http import JsonResponse   
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Movies
from .models import Directors
from .models import Country

#-----------------------------------------------------------------------------------
#CRUD OF MOVIES MODEL

@csrf_exempt
def getMovies(request):
    if request.method=='GET':
        allmovies=Movies.objects.all()
      
        return JsonResponse(allmovies)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


@csrf_exempt  
def getMoviesId(request, movieId):
        
    movie = get_object_or_404(Movies, id=movieId)
    country = get_object_or_404(Country, id=movieId)
    director = get_object_or_404(Directors, id=movieId)
    return JsonResponse({
            'Movie' : movie.title,
            'Year': movie.year,
            'Country': country.name,
            'Director': director.name,
            'Studio': movie.studio,
    })

@csrf_exempt
def postMovies(request):
    
    if request.method == 'POST':
        
        json_data = json.loads(request.body.decode('utf-8'))
        
        country_id = json_data.get('country_id')
        country_instance = get_object_or_404(Country, id=country_id)
        
        director_id = json_data.get('director_id')
        director_instance = get_object_or_404(Directors, id=director_id)
        
        newMovie = Movies(
            title=json_data.get('title', ''),
            year=json_data.get('year', ''),
            country=country_instance,
            director=director_instance,
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
    
#-------------------------------------------------------------------------------------
#CRUD OF DIRECTORS
@csrf_exempt
def getDirectorsId(request, directorId):
    ifrequest=directorId
    if ifrequest==True:
        director = get_object_or_404(Directors, id=directorId)
        directornumber = director.id
        directorName = director.nameD
        return JsonResponse({
            'Director number' : directornumber,
            'Name': directorName,
    })
    else:
        
        return JsonResponse({'status': 'error', 'message': f'Director number {directorId} not found'}, status=404)

@csrf_exempt
def postDirectors(request):
    
    if request.method == 'POST':
        
        json_data = json.loads(request.body.decode('utf-8'))

        newDirector = Directors(
            nameD=json_data.get('name', ''),
        )
        newDirector.save()
        return JsonResponse({'status': 'success', 'message': 'Director Added'})

    else:
        
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
    
@csrf_exempt
def deleteDirectors(request, directorId):
    
    if request.method=='DELETE':
        
        director = get_object_or_404(Directors, id=directorId)

        
        director.delete()
            
        return JsonResponse({'message': f'Director number "{directorId}" deleted successfully!'})
    
    else:
        return JsonResponse({'error': f'Director number "{directorId}" not fofound'}, status=404)
    
@csrf_exempt
def putDirectors(request, directorId):
    ifrequest=directorId
    if request.method=='PUT':
        
        json_data = json.loads(request.body.decode('utf-8'))
        director = get_object_or_404(Directors, id=directorId)

        director.nameD = json_data.get('Name', '')
        director.save()

        return JsonResponse({'status': 'success', 'message': 'Director Data Changed'})
    # elif ifrequest==False:
    #     return JsonResponse({'status': 'error', 'message': 'Nuber not Found'})
    # elif request.method!='PUT':
    #     return JsonResponse({'status': 'error', 'message': 'The method is not PUT'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
    #----------------------------------------------------------------------------------
    #Countrys
    
@csrf_exempt
def postCountrys(request):
    
    if request.method == 'POST':
        
        json_data = json.loads(request.body.decode('utf-8'))

        newCountry = Country(
            nameC=json_data.get('name', ''),    
            
        )
        newCountry.save()
        
        return JsonResponse({'status': 'success', 'message': 'Country Added'})

    else:
        
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
    
