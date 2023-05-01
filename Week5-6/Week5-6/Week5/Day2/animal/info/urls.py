from django.urls import path 
from . import views 

# one urlpattern per line
urlpatterns = [
    # path('', views.animals['id'], name='animal'),
    path('family/<int:id>', views.families, name='family'),
    path('animal/<int:id>', views.animals, name='one_animal'),
    path('animals/', views.all_animals, name='animals_all'),
    
]