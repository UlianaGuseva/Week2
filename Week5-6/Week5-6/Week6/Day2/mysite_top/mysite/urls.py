from django.contrib import admin
from django.urls import path, include
from polls.views import PostCreateView, PostListView, PostView, PostUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("add-post/", PostCreateView.as_view()),
    path("posts/", PostListView.as_view(), name="posts-all"),
    path("post/<int:pk>", PostView.as_view(), name="post"), 
    path("post-update/<int:pk>", PostUpdateView.as_view()),
    path('accounts/', include('accounts.urls')),
    
]
