"""
URL configuration for work project.

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
from django.urls import path, include
from managment.views import DepartmentDetailAPIView ,DepartmentCreateAPIView, DepartmentListAPIView, EmployeeListAPIView, EmployeeCreateAPIView, ProjectRetrieveAPIView, ProjectUpdateAPIView, TaskRetrieveAPIView, TaskUpdateAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('departments/', DepartmentListAPIView.as_view(), name='all_departments'),
    path('departments/create/', DepartmentCreateAPIView.as_view(), name='create_department'),
    path('departments/details/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),    
    path('employee/', EmployeeListAPIView.as_view(), name='all_employee'),
    path('employee/create/', EmployeeCreateAPIView.as_view(), name='create_employee'),
    path('projects/<int:pk>/', ProjectRetrieveAPIView.as_view(), name='get_project'),
    path('projects/update/<int:pk>/', ProjectUpdateAPIView.as_view(), name='update_project'),
    path('task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='get_task'),
    path('task/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='update_task'),
]
