from django.shortcuts import render
from .models import Gif, Category
from .forms import GifForm, CategoryForm

# Create your views here.
def Homepage(request):
    context = {'data': Gif.objects.all()}
    return  render(request, 'index_home.html', context)

def all_categories(request):
    context = {'data': Category.objects.all()}
    return  render(request, 'all_categories.html', context)

def add_gif(request):
    if request.method == 'POST':
        gif_filled_form = GifForm(request.POST)
        if gif_filled_form.is_valid():
            new_gif = gif_filled_form.save()
            category = gif_filled_form.cleaned_data['categories']
            category_obj = Category.objects.get(name=category)
            new_gif.categories.add(category_obj)
        
    gif_form = GifForm()   
    context = {'form' : gif_form}
    gif_filled_form = GifForm(request.POST)
    
    return render(request, 'add_gif.html', context)

def add_category(request):
    if request.method == 'POST':
        cat_filled_form = CategoryForm(request.POST)
        if cat_filled_form.is_valid():
            cat_filled_form.save()
        
    cat_form = CategoryForm()   
    context = {'form' : cat_form}
    cat_filled_form = CategoryForm(request.POST)
    
    return render(request, 'add_category.html', context)
    
def get_category(request, id):
    category = Category.objects.get(id=id)
    gifs = category.gifs.all()    
    context = {'gifs': gifs}
    return render(request, 'get_category.html', context)

def get_gif(request, id):
    gif = Gif.objects.get(id=id)   
    if request.method == 'POST':
        like = int(request.POST.get('like', 0))
        gif.likes += like
        gif.save()
    context = {'gif': gif}
    return render(request, 'get_gif.html', context)
    
def best(request):
    
    context = {'data': Gif.objects.filter(likes__gt=0).order_by('-likes')}
    return render(request, 'best_gifs.html', context)
