from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from datetime import date
from django.views import generic
from .models import Post
from .forms import PostForm

# CRUD - CREATE - RETRIEVE - UPDATE - DELETE

class PostCreateView(generic.CreateView):

    template_name = 'create_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("posts-all")

class PostUpdateView(generic.UpdateView):

    template_name = 'update_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("posts-all")

class PostListView(generic.ListView):

    template_name = 'post_list.html'
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['current_date'] = date.today()
        return context

class PostView(generic.DetailView):

    template_name = 'post.html'
    context_object_name = 'post'
    model = Post

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        return context
    