from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Space 
import requests 
import json
API_KEY = 'dXrxMJfWAGWQ1WbP2K447FTAKr3VUfBuDf6GV88I'



# def pics_index(request):
#   url =f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'
#   response = requests.get(url)
#   data = response.json()
#   pics = data['hdurl']
#   date = data['date']
#   title = data['title']
#   context = {'pics': pics, 'date': date, 'title': title}
#   return render(request, 'pics/index.html', context )


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pics_index(request):
  return render(request, 'pics/index.html')

def pics_create_page(request):
  return render (request, 'main_app/space_form.html')


def pics_create(request):
  date_query = request.GET.get('date')
  url =f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date_query}'
  response = requests.get(url)
  data = response.json()
  date = data['date']
  url = data['hdurl']
  title = data['title']
  print('HERE IS THE DATA', url, date, title)
  context = {'date': date, 'url': url, 'title': title}
  return render(request, 'main_app/space_form.html', context)

class Home(LoginView):
  template_name = 'home.html'

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
