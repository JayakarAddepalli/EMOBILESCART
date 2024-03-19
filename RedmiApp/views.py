from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from APP.models import *
from django.contrib import messages
from django.urls import reverse


# Create your views here.
@login_required(login_url='APP:login')
def RedmiCategoriesView(request):
    redmidata = Redmi.objects.all()
    return render(request, 'Redmicategories.html', {'rd' : redmidata})

def RedmiCategoriesViewItem(request, slug):
    if(Redmi.objects.filter(slug=slug)):
        products = Redmi.objects.filter(slug = slug)
        data = {'products':products}
        return render(request, "applepro.html", context= data)
    # messages.warning(request, "No such product")
    return redirect(reverse('RedmiApp:redmicategories', kwargs={'slug': slug}))