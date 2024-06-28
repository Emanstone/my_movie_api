from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details  # Here for importing the function based view

from watchlist_app.api.views import MovieListAV, MovieDetail    # Here for importing the class based views


urlpatterns = [
    # path('list/', movie_list, name='movie-list'),   # Here for mapping the function based views
    # path('<int:pk>', movie_details, name='movie-detail'),

    path('list/', MovieListAV.as_view(), name='movie-list'),   # Here for mapping the class based views
    path('<int:pk>', MovieDetail.as_view(), name='movie-detail'),
]