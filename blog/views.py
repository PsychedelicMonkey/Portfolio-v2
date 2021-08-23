from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
  model = Post
  ordering = '-created_at'
  context_object_name = 'posts'
  template_name = 'blog/blog.html'
  paginate_by = 20

class PostDetail(DetailView):
  model = Post
  context_object_name = 'post'
  template_name = 'blog/post.html'