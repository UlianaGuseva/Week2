"""
URL configuration for weather_report project.

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
from weatherapp.views import ReportView, ReportMixinView, ReportListView, ReportDetailView, ForecasterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/reports/', ReportView.as_view(), name='reports'),
    path('api/reports/<int:pk>', ReportView.as_view(), name='reports'),
    path('mixin/reports/', ReportMixinView.as_view(), name='reports_mixins'),
    path('generic/reports/', ReportListView.as_view(), name='reports_generic'),
    path('generic/reports/<int:pk>', ReportDetailView.as_view(), name='report_generic'),
    path('api/forecaster/<int:pk>', ForecasterView.as_view(), name='forecaster'),
]
