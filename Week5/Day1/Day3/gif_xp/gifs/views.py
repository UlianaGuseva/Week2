from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.template import loader
from .forms import Gif, Category

# Create your views here.
def Homepage(request):
    context = {'data': models.Gif.objects.all()}
    return  render(request, 'index_home.html', context)

def add_gif(request):
    context = {
        'form' : Gif()
    }
    return render(request, 'add_gif.html', context)

def add_category(request):
    context = {
        'form' : Category()
    }
    return render(request, 'add_category.html', context)
    
def get_category(request, id):
    category = models.Category.objects.get(id=id)
    gifs = category.gifs.all()    
    context = {'gifs': gifs}
    return render(request, 'get_category.html', context)

def get_gif(request, id):
    gif = models.Gif.objects.get(id=id)   
    context = {'gif': gif}
    return render(request, 'get_gif.html', context)
    



