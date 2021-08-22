from typing import List
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.views.generic import ListView
from .forms import EmailForm
from .models import Photo

def index(request):
  if request.POST:
    form = EmailForm(request.POST)
    if form.is_valid():
      msg = form.cleaned_data
      send_mail(
        msg['subject'],
        msg['body'],
        msg['email'],
        ['admin@example.com'] # send to the website owner
      )
      return redirect('index')
  else:
    form = EmailForm()
  photos = Photo.objects.all()[:8]
  context = {
    'title': 'Home',
    'form': form,
    'photos': photos,
  }
  return render(request, 'gallery/index.html', context)

class GalleryView(ListView):
  model = Photo
  ordering = '-created_at'
  template_name = 'gallery/gallery.html'
  context_object_name = 'photos'
