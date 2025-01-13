from django.shortcuts import render

# Create your views here.
from .models import Movies
from django.core.paginator import Paginator


def movie_list(request):
    movie_object=Movies.objects.all()
    paginator = Paginator(movie_object,4)
    page= request.GET.get('page')
    movie_object = paginator.get_page(page)
    return render(request,'movies_list.html',{'movie_object':movie_object})