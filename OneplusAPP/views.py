from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from APP.models import *
from django.urls import reverse
from django.contrib import messages

# Create your views here.
@login_required(login_url='APP:login')
def OneplusCategoriesView(request):
    oneplusdata = Oneplus.objects.all()
    return render(request, 'Onepluscategories.html', {'od' : oneplusdata})

def OneplusCategoriesViewItem(request, slug):
    if(Oneplus.objects.filter(slug=slug)):
        products = Oneplus.objects.filter(slug = slug)
        data = {'products':products}
        return render(request, "applepro.html", context= data)
    # messages.warning(request, "No such product")
    return redirect(reverse('OneplusAPP:Onepluscategories', kwargs={'slug': slug}))
