"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental/', views.rental, name='all_rental'),
    path('rent/rental/<int:id>', views.rental_details, name='one_rental'),
    path('rent/rental/add', views.rental_add, name='add_rental'),
    path('rent/customer/<int:id>', views.customer_find, name='one_customer'),
    path('rent/customer/', views.customer_all, name='all_customers'),
    path('rent/customer/add', views.customer_add, name='add_customers'),
    path('rent/vehicle/', views.vehicle_all, name='all_vehicle'),
    path('rent/vehicle/<int:id>', views.vehicle_find, name='one_vehicle'),
    path('rent/vehicle/add', views.vehicle_add, name='add_vehicle'),    
    path('rent/home', views.home, name='home')    
    
    
]
