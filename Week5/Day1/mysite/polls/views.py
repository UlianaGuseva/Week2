from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
# Create your views here.

def index(request):
    # return HttpResponse("<h1>Home page</h1>")
    current_time = date.today()
    current_hour = datetime.now().hour
    context = {'weather': 'warm', 'current_date': current_time, 'current_hour': current_hour}
    return render(request, 'index.html', context)