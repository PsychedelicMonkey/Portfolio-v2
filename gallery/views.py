from django.shortcuts import render
from .models import Photo

def index(request):
  photos = Photo.objects.all()[:8]
  context = {
    'title': 'Home',
    'photos': photos,
  }
  return render(request, 'gallery/index.html', context)
