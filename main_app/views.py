from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Space 
import requests 
API_KEY = 'dXrxMJfWAGWQ1WbP2K447FTAKr3VUfBuDf6GV88I'

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('pics_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def pics_index(request):
  url =f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'
  response = requests.get(url)
  data = response.json()
  print(data)
  context = {'data': data}
  return render(request, 'pics/index.html', context )
  # return render(request, 'pics/index.html', {'pics': pics})

