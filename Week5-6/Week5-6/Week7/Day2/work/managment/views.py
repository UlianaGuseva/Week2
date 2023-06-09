from django.shortcuts import render
from .models import Department, Employee, Task, Project
from .serializers import DepartmentSerializer, EmployeeSerializer, TaskSerializer, ProjectSerializer, DepartmentUrlsSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .permissions import IsDepartmentAdmin
# Create your views here.

class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentUrlsSerializer
  
 
class DepartmentDetailAPIView(RetrieveAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer    
    
class DepartmentCreateAPIView(CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    
    
class ProjectRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class ProjectUpdateAPIView(UpdateAPIView, DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class TaskRetrieveAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskUpdateAPIView(UpdateAPIView, DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
    