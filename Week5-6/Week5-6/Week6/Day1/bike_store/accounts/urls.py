from django.urls import path
from .views import SignUpView, ProfileView,  create_profile_view, profile_redirect_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile-page'),
    path('create_profile/', create_profile_view, name='create_profile'),
    path('profile_redirect/', profile_redirect_view, name='profile_redirect')
]