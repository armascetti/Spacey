from django.urls import path 
from . import views 


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name="about"),
  path('pics/', views.pics_index, name='pics_index'),
  path('accounts/signup/', views.signup, name='signup'),
  path('pics/create/', views.pics_create, name='pics_create'),
]