from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from polls.views import PostCreateView, PostListView, PostView, PostUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path("add-post/", PostCreateView.as_view()),
    path("posts/", PostListView.as_view(), name="posts-all"),
    path("post/<int:pk>", PostView.as_view(), name="post"), 
    path("post-update/<int:pk>", PostUpdateView.as_view()),
]

