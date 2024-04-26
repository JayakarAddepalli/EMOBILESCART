from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from APP.models import *
from django.contrib import messages


# Create your views here.

@login_required(login_url='APP:login')
def CategoriesView(request):
    appledata = Apple.objects.all()
    messages.info(request, 'item added')
    return render(request, 'categories.html', {'ad': appledata})

def CategoriesViewItem(request, slug):
    if(Apple.objects.filter(slug=slug)):
        products = Apple.objects.filter(slug = slug)
        data = {'products':products}
        return render(request, "applepro.html", context= data)
    # messages.warning(request, "No such product")
    return redirect(reverse('AppleApp:categories', kwargs={'slug': slug}))

# def apple_add_to_cart(request, id):
#     product = Apple.objects.filter(id=id)

#     li = [
#         CartItem(product = product[0], user = request.user)
#     ]
#     CartItem.objects.bulk_create(li)
    
#     # cart_item.save()
#     return render(request, 'cart.html', {'p':product})



    