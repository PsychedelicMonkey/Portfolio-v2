from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  cover_image = models.ForeignKey('Photo', on_delete=models.CASCADE, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Photo(models.Model):
  title = models.CharField(max_length=100, null=True, blank=True)
  caption = models.TextField(null=True, blank=True)
  image = models.ImageField(null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)

  categories = models.ManyToManyField(Category, blank=True)
