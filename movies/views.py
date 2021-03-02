from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

from django.core.paginator import Paginator
# Create your views here.


class MovieViewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ActionViewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='action')
    serializer_class = MovieSerializer


class ComedyViewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='comedy')
    serializer_class = MovieSerializer


def movie_list(request):
    movie_objects = Moviedata.objects.all()
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains=movie_name)

    paginator = Paginator(movie_objects, 3)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)

    return render(request, 'movies/movie_list.html', {'movie_objects': movie_objects})
