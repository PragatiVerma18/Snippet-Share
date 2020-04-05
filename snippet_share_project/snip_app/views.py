from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Snip
from .forms import snipForm



def show_snip(request,link_c):
    snips=Snip.objects.order_by('-updated_at')[:10]
    snip=Snip.objects.get(link_code=link_c)
    return render(request, "detail.html", {'snip': snip,'snips':snips})

def all(request):
    snips = Snip.objects.all()
    return render(request, 'all.html', {'snips': snips})

def index(request):
    snips=Snip.objects.order_by('-updated_at')[:8]
    form=snipForm()
    if request.method=="POST":
        try:
            form=snipForm(request.POST)
            form.save()
            return HttpResponseRedirect("/") 
        except ValueError:
            pass

    return render(request, "index.html", {'form':form, 'snips':snips})