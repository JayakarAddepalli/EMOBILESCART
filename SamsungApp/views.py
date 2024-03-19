from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from APP.models import *
from django.urls import reverse
from django.contrib import messages


# Create your views here.

@login_required(login_url='APP:login')
def SamsungCategoriesView(request):
    samsungdata = Samsung.objects.all()
    return render(request, 'Samsungcategories.html', {'sd' : samsungdata})


def SamsungCategoriesViewItem(request, slug):
    if(Samsung.objects.filter(slug=slug)):
        products = Samsung.objects.filter(slug = slug)
        data = {'products':products}
        return render(request, "applepro.html", context= data)
    # messages.warning(request, "No such product")
    return redirect(reverse('SamsungApp:samsungcategories', kwargs={'slug': slug}))