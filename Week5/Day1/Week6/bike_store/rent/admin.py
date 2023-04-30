from django.contrib import admin
from .models import Vehicle_Type, Vehicle_Size, Rental_Rate, Vehicle
# Register your models here.
admin.site.register(Vehicle_Type)
admin.site.register(Vehicle_Size)
admin.site.register(Rental_Rate)
admin.site.register(Vehicle)

