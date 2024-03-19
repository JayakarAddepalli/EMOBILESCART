from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from APP.models import *
from django.urls import reverse
from django.contrib import messages

# Create your views here.
@login_required(login_url='APP:login')
def RealmeCategoriesView(request):
    realmedata = Realme.objects.all()
    return render(request, 'Realmecategories.html', {'red' : realmedata})

def RealmeCategoriesViewItem(request, slug):
    if(Realme.objects.filter(slug=slug)):
        products = Realme.objects.filter(slug = slug)
        data = {'products':products}
        return render(request, "applepro.html", context= data)
    # messages.warning(request, "No such product")
    return redirect(reverse('RealmeApp:realmecategories', kwargs={'slug': slug}))