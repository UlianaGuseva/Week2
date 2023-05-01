from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView, SignUpView, create_profile_view, profile_redirect_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('create-profile/', create_profile_view, name='create_profile'),
    path('profile-redirect/', profile_redirect_view, name='profile-redirect')
]

