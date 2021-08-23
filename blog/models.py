from django.db import models
from django.contrib.auth.models import User
from gallery.models import Photo

class Post(models.Model):
  title = models.CharField(max_length=100, null=False, blank=False)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField(null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  photos = models.ManyToManyField(Photo, related_name='post')

  def __str__(self):
    return self.title
  