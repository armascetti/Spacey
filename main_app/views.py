from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Space:
  def __init__(self, date, title, url,):
    self.date = date
    self.title = title
    self.url = url 


pics = [
  Space('date', 'title', 'url')
]

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
  return render(request, 'pics/index.html', { 'pics': pics })