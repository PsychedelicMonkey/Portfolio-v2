from django.db import models

class Photo(models.Model):
  title = models.CharField(max_length=100, null=True, blank=True)
  caption = models.TextField(null=True, blank=True)
  image = models.ImageField(null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
