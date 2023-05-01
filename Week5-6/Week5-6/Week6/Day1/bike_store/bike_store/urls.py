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
    path('rent/rental/', views.ShowAllRentals.as_view(), name='all_rental'),
    path('rent/rental/<int:pk>', views.RentalDetails.as_view(), name='one_rental'),
    path('rent/rental/add', views.AddRental.as_view(), name='add_rental'),
    path('rent/customer/<int:pk>', views.FindCustomer.as_view(), name='one_customer'),
    path('rent/customer/', views.AllCustomers.as_view(), name='all_customers'),
    path('rent/customer/add', views.AddCustomer.as_view(), name='add_customers'),
    path('rent/vehicle/', views.AllVehicle.as_view(), name='all_vehicle'),
    path('rent/vehicle/<int:pk>', views.FindVehicleView.as_view(), name='one_vehicle'),
    path('rent/vehicle/add', views.AddVehicle.as_view(), name='add_vehicle'),    
    path('rent/home', views.home, name='home')    
    
    
]
