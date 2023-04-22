from django.urls import path 
from . import views 

# one urlpattern per line
urlpatterns = [
    path('<int:id>', views.people_info, name='peopleinfo'),
    path('', views.people_all, name='peopleall'),
    
]