from django.contrib import admin
from .models import Project, Department, Employee, Task
# Register your models here.
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Task)