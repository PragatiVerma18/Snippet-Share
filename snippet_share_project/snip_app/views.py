from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Snip
from .forms import snipForm, searchForm
from .EncodeDecodeURL import EncodeDecodeURL


def show_snip(request,link_c):
    snips=Snip.objects.order_by('-updated_at')[:10]
    if Snip.objects.get(link_code=link_c).private==True and Snip.objects.get(link_code=link_c).user==request.user:
        snip=Snip.objects.get(link_code=link_c)
    else:    
        snip=Snip.objects.get(link_code=link_c,private=False)
    searchform=searchForm()
    if request.method=="POST":
        try:
            searchform=searchForm(request.POST)
            x = request.POST['search']
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, "detail.html", {'searchform':searchform,'snip': snip,'snips':snips})

def all(request):
    if request.user.is_authenticated:
        snips= Snip.objects.filter(private=False) | Snip.objects.filter(user=request.user,private=True)
    else:
        snips = Snip.objects.filter(private=False)
    searchform=searchForm()
    if request.method=="POST":
        try:
            searchform=searchForm(request.POST)
            x = request.POST['search']
            x = EncodeDecodeURL(x).encode()
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, 'all.html', {'searchform':searchform,'snips': snips})

def index(request):
    if request.user.is_authenticated:
        snips=Snip.objects.filter(private=False).order_by('-updated_at')[:8] | Snip.objects.filter(private=True,user=request.user).order_by('-updated_at')[:8]
        form=snipForm1()
    else:
        snips=Snip.objects.filter(private=False).order_by('-updated_at')[:8]
        form=snipForm()
    if request.method=="POST":
        try:
            if request.user.is_authenticated:
                form=snipForm1(request.POST)
                p=form.save(commit=False)
                p.user=request.user
                p.save()
            else:
                form=snipForm(request.POST)
                form.save()
            return HttpResponseRedirect("/") 
        except ValueError:
            pass
    searchform=searchForm()
    if request.method=="POST":
        try:
            searchform=searchForm(request.POST)
            x = request.POST['search']
            x = EncodeDecodeURL(x).encode()
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, "index.html", {'searchform':searchform,'form':form, 'snips':snips})

def search(request, link_c):
    link_c = EncodeDecodeURL(link_c).decode()
    snips= Snip.objects.filter(link_code=link_c)
    form=searchForm()
    if request.method=="POST":
        try:
            form=searchForm(request.POST)
            x = request.POST['search']
            x = EncodeDecodeURL(x).encode()
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, "all.html", {'searchform':form,'snips':snips})
