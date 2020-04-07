from django.shortcuts import render,redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from snip_app.forms import searchForm
from snip_app.models import Snip

def signup(request):
  snips=Snip.objects.order_by('-updated_at')[:8]
  searchform=searchForm()
  if request.method=="POST":
    try:
      searchform=searchForm(request.POST)
      x = request.POST['search']
      return HttpResponseRedirect("/search/"+x) 
    except ValueError:
      pass
  if request.method == 'POST':
    if request.POST['password'] == request.POST['confirmpassword']:
      try:
        user = User.objects.get(username = request.POST['username'])
        return render(request, 'accounts/signup.html', {'error' : 'Username has been already taken', 'searchform':searchform, 'snips':snips})
      except User.DoesNotExist:
        user = User.objects.create_user(username =request.POST['username'], password=request.POST['password'])
        auth.login(request, user)
        return redirect('index')
    else:
      return render(request, 'accounts/signup.html', {'error' : 'Passwords must match', 'searchform':searchform,'snips':snips})

  else:
    return render (request, 'accounts/signup.html', {'searchform':searchform,'snips':snips})

def login(request):
  snips=Snip.objects.order_by('-updated_at')[:8]
  searchform=searchForm()
  if request.method=="POST":
    try:
      searchform=searchForm(request.POST)
      x = request.POST['search']
      return HttpResponseRedirect("/search/"+x) 
    except ValueError:
      pass
  if request.method == 'POST':
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      auth.login(request, user)
      return redirect('index')
    else:
      return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.','searchform':searchform,'snips':snips})
  else:
    return render (request, 'accounts/login.html', {'searchform':searchform,'snips':snips})

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('index')

