from django.urls import path
from . import views

urlpatterns = [
  path('', views.PostList.as_view(), name='blog'),
  path('<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
  path('archive/<int:year>/', views.PostYearArchive.as_view(), name='post-year-archive'),
  path('archive/<int:year>/<int:month>/', views.PostMonthArchive.as_view(month_format='%m'), name='post-month-archive'),
]