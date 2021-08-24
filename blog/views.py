from django.shortcuts import render
from django.views.generic import ListView, DetailView, YearArchiveView, MonthArchiveView
from .models import Post

class PostList(ListView):
  model = Post
  ordering = '-created_at'
  queryset = Post.objects.all()
  date_field = 'created_at'
  context_object_name = 'posts'
  template_name = 'blog/blog.html'
  paginate_by = 20

class PostDetail(DetailView):
  model = Post
  context_object_name = 'post'
  template_name = 'blog/post.html'

class PostYearArchive(YearArchiveView):
  queryset = Post.objects.all()
  date_field = 'created_at'
  make_object_list = True
  template_name = 'blog/year.html'
  paginate_by = 20

  def get_context_data(self, **kwargs):
    context = super(PostYearArchive, self).get_context_data(**kwargs)
    context['year'] = self.kwargs.get('year')
    return context

class PostMonthArchive(MonthArchiveView):
  queryset = Post.objects.all()
  date_field = 'created_at'
  make_object_list = True
  template_name = 'blog/month.html'
  paginate_by = 20

  def get_context_data(self, **kwargs):
    context = super(PostMonthArchive, self).get_context_data(**kwargs)
    context['year'] = self.kwargs.get('year')
    return context
