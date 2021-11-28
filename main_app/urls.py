from django.urls import path 
from . import views 


urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.about, name="about"),
  path('pics/', views.pics_index, name='pics_index'),
  path('pics/create', views.pics_create_page, name='pics_create_page'),
  path('pics/create/new', views.pics_create, name='pics_create'),
  path('accounts/signup/', views.signup, name='signup'),
  path('', views.Home.as_view(), name="home"),
]