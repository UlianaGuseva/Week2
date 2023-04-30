from django.contrib import admin

from .models import Person

class PersonAdmin(admin.ModelAdmin):
        fields = ['name', 'email', 'phone_number', 'address']
        search_fields = ['name']

admin.site.register(Person, PersonAdmin)
