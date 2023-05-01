from django.shortcuts import render
from .models import Todo, Category
from .forms import TodoForm
from datetime import date
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def todo(request):
    if request.method == 'POST':
        gif_filled_form = TodoForm(request.POST)
        if gif_filled_form.is_valid():
            gif_filled_form.save()
    
    todo_form = TodoForm()   
    context = {'form' : todo_form}
    gif_filled_form = TodoForm(request.POST)
    
    return render(request, 'index_todo.html', context)

def display_todos(request):
    context = {'data': Todo.objects.filter(has_been_done=False)}
    return render(request, 'list_todo.html', context)

def done(request, id):
    task = Todo.objects.get(id=id)
    task.has_been_done = True
    task.date_completion = date.today()
    task.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/list/')
    
    
