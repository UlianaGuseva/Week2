from .models import Department, Employee, Task, Project
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class EmployeeUrlsSerializer(serializers.ModelSerializer):
    department = serializers.HyperlinkedIdentityField(view_name='get_department')
    class Meta:
        model = Employee
        fields = '__all__'
        
# class DepartmentUrlsSerializer(serializers.ModelSerializer):
#     id = serializers.HyperlinkedIdentityField(view_name='get_department')
#     class Meta:
#         model = Department
#         fields = '__all__'
        
