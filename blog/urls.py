from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('data/', views.data, name='blog-data'),

  
]
