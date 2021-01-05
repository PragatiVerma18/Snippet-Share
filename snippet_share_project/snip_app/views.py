from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Snip
from .forms import snipForm, searchForm



def show_snip(request,link_c):
    snips=Snip.objects.order_by('-updated_at')[:10]
    snip=Snip.objects.get(link_code=link_c)
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
    snips = Snip.objects.all()
    searchform=searchForm()
    if request.method=="POST":
        try:
            searchform=searchForm(request.POST)
            x = request.POST['search']
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, 'all.html', {'searchform':searchform,'snips': snips})

def index(request):
    snips=Snip.objects.order_by('-updated_at')[:8]
    form=snipForm(initial={'author':request.user})
    if request.method=="POST":
        try:
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
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass

    return render(request, "index.html", {'searchform':searchform,'form':form, 'snips':snips})

def search(request, link_c):
    snips= Snip.objects.filter(link_code=link_c)
    form=searchForm()
    if request.method=="POST":
        try:
            form=searchForm(request.POST)
            x = request.POST['search']
            return HttpResponseRedirect("/search/"+x) 
        except ValueError:
            pass
    return render(request, "all.html", {'searchform':form,'snips':snips})

def delete_snippet(request,snippet_id):
    del_obj=Snip.objects.get(link_code=snippet_id)
    del_obj.delete()
    return HttpResponseRedirect('/all/')

