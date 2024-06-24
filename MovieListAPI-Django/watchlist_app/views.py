from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse


def movie_list(request):
    movies = Movie.objects.all()
    # print(movies.values())                    #1
    # list(movies.values())  # convert to list  #2
    # data = {'movies': list(movies.values())}  #3
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)



def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)
