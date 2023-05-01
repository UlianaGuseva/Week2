from django.urls import path 
from . import views 

# one urlpattern per line
urlpatterns = [
    # path('', views.animals['id'], name='animal'),
    path('family/<int:id>', views.families, name='family'),
    path('animal/<int:id>', views.animals, name='animal')
    
]