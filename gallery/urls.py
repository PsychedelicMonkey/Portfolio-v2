from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('category/<str:name>/', views.CategoryPhotoView.as_view(), name='category-photos'),
  path('category/', views.CategoryView.as_view(), name='category'),
  path('gallery/', views.GalleryView.as_view(), name='gallery'),
]
