from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='APP:login')
def HomeView(request):
    data = Trends.objects.all()
    return render(request, 'home.html', {'d':data})



def RegisterView(request):
    if request.method == 'POST':
        user = User.objects.filter(username = request.POST['username'])
        if user.exists():
            messages.info(request, 'username already exist')
            return redirect(reverse('APP:register'))
        
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('APP:login'))
        
    form = Register()
    return render(request, 'register.html', {'f':form})

def CusLoginView(request):
    if request.method == 'POST':
        f = Login(request.POST)
        if f.is_valid():
            user = authenticate(username = f.cleaned_data['username'], password = f.cleaned_data['password'])
            if user:
                login(request, user)
                return render(request, 'home.html', {'u':user})
            else:
                messages.info(request, 'invalid username or password')
                return redirect(reverse('APP:login'))
    f = Login()
    return render(request, 'login.html', {'f':f})

def UserView(request):
    return render(request, 'user.html')

def CusLogoutView(request):
    logout(request)
    return redirect(reverse('APP:user'))

def APPLEBUYNOWVIEW(request, id):

    appleproduct = Apple.objects.get(id=id)
    
    cartitem, created = CartItem.objects.get_or_create(appleproduct = appleproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()

    return redirect(reverse('APP:viewcart'))


def ONEPLUSBUYNOWVIEW(request, id):

    oneplusproduct = Oneplus.objects.get(id=id)
    

    cartitem, created = OneplusCartItem.objects.get_or_create(oneplusproduct = oneplusproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()

    return redirect(reverse('APP:viewcart'))


def SAMSUNGBUYNOWVIEW(request, id):

    samsungproduct = Samsung.objects.get(id=id)
    

    cartitem, created = SamsungCartItem.objects.get_or_create(samsungproduct = samsungproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()

    return redirect(reverse('APP:viewcart'))

def REDMIBUYNOWVIEW(request, id):

    redmiproduct = Redmi.objects.get(id=id)
    

    cartitem, created = RedmiCartItem.objects.get_or_create(redmiproduct = redmiproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()
    
    return redirect(reverse('APP:viewcart'))


def REALMEBUYNOWVIEW(request, id):

    realmeproduct = Realme.objects.get(id=id)
    

    cartitem, created = RealmeCartItem.objects.get_or_create(realmeproduct = realmeproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()
    
    return redirect(reverse('APP:viewcart'))


# def view_cart(request):
#     # ap = Apple.objects.filter(slug=slug)
#     cart_item = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.product.Cost for item in cart_item)
#     return render(request, 'cart.html', {'cart_item':cart_item, 'total_cost':total_price})

@login_required(login_url='APP:login')
def viewcart(request):
    cartitems = CartItem.objects.filter(user = request.user)
    applesum = sum(item.appleproduct.Cost * item.quantity for item in cartitems)

    onepluscartitem = OneplusCartItem.objects.filter(user = request.user)
    oneplussum = sum(item.oneplusproduct.Cost * item.quantity for item in onepluscartitem)

    samsungcartitem = SamsungCartItem.objects.filter(user = request.user)
    samsungsum = sum(item.samsungproduct.Cost * item.quantity for item in samsungcartitem)

    redmicartitem = RedmiCartItem.objects.filter(user = request.user)
    redmisum = sum(item.redmiproduct.Cost * item.quantity for item in redmicartitem)


    realmecartitem = RealmeCartItem.objects.filter(user = request.user)
    realmesum = sum(item.realmeproduct.Cost * item.quantity for item in realmecartitem)

    totalprize = applesum + oneplussum + samsungsum + redmisum + realmesum

    if(request.method == 'POST'):
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    form = PaymentForm()

    return render(request, 'cart.html', {'form':form, 'cartitems':cartitems, 'onepluscartitem':onepluscartitem, 'samsungcartitem':samsungcartitem, 'redmicartitem':redmicartitem, 'realmecartitem':realmecartitem, 'appletotalprize':applesum, 'oneplustotalprize':oneplussum, 'samsungtotalprize':samsungsum, 'redmitotalprize':redmisum, 'realmetotalprize':realmesum, 'totalprize':totalprize})

@login_required(login_url='APP:login')
def successviewcheck(request):
    if(request.method == 'POST'):
        form = PaymentForm(request.POST)
        if form:
            if form.is_valid():
                form.save(commit=True)
                return redirect(reverse('APP:successpage'))
        else:
            return redirect(reverse('APP:viewcart'))

    form = PaymentForm()
    return render(request, 'cart.html', {'f':form})
   

@login_required(login_url='APP:login')
def successpageview(request):
    return render(request, 'successpage.html')

#==============================apple cart==================================
def addtocartview(request, slug=None, id=None):
    appleproduct = Apple.objects.get(id=id)
    
    cartitem, created = CartItem.objects.get_or_create(appleproduct = appleproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()
    

    return redirect(reverse('AppleApp:categories'))

def removeitemcart(request, id):
    r = CartItem.objects.filter(id = id, user = request.user)
    r.delete()

    return redirect(reverse('APP:viewcart'))

def incrementitem(request , appleproduct):
    r = CartItem.objects.get(appleproduct = appleproduct, user = request.user)
    r.quantity += 1
    r.save()

    return redirect(reverse('APP:viewcart'))

def decrementitem(request , appleproduct):
    r = CartItem.objects.get(appleproduct = appleproduct, user = request.user)
    
    if (r.quantity > 1):
        r.quantity -= 1
    r.save()

    return redirect(reverse('APP:viewcart'))
#==============================oneplus cart==================================

def oneplusaddtocartview(request, slug=None, id=None):
    oneplusproduct = Oneplus.objects.get(id=id)
    

    cartitem, created = OneplusCartItem.objects.get_or_create(oneplusproduct = oneplusproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()

    return redirect(reverse('OneplusAPP:Onepluscategories'))


def oneplusremoveitemcart(request, id):
    r = OneplusCartItem.objects.filter(id = id, user = request.user)
    r.delete()

    return redirect(reverse('APP:viewcart'))


def oneplusincrementitem(request , oneplusproduct):
    r = OneplusCartItem.objects.get(oneplusproduct = oneplusproduct, user = request.user)
    r.quantity += 1
    r.save()

    return redirect(reverse('APP:viewcart'))

def oneplusdecrementitem(request , oneplusproduct):
    r = OneplusCartItem.objects.get(oneplusproduct = oneplusproduct, user = request.user)
    
    if (r.quantity > 1):
        r.quantity -= 1
    r.save()

    return redirect(reverse('APP:viewcart'))

#==============================samsung cart==================================

def samsungaddtocartview(request, slug=None, id=None):
    samsungproduct = Samsung.objects.get(id=id)
    

    cartitem, created = SamsungCartItem.objects.get_or_create(samsungproduct = samsungproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()

    return redirect(reverse('SamsungApp:samsungcategories'))


def samsungremoveitemcart(request, id):
    r = SamsungCartItem.objects.filter(id = id, user = request.user)
    r.delete()

    return redirect(reverse('APP:viewcart'))


def samsungincrementitem(request , samsungproduct):
    r = SamsungCartItem.objects.get(samsungproduct = samsungproduct, user = request.user)
    r.quantity += 1
    r.save()

    return redirect(reverse('APP:viewcart'))

def samsungdecrementitem(request , samsungproduct):
    r = SamsungCartItem.objects.get(samsungproduct = samsungproduct, user = request.user)
    
    if (r.quantity > 1):
        r.quantity -= 1
    r.save()

    return redirect(reverse('APP:viewcart'))


#==============================redmi cart==================================

def redmiaddtocartview(request, slug=None, id=None):
    redmiproduct = Redmi.objects.get(id=id)
    

    cartitem, created = RedmiCartItem.objects.get_or_create(redmiproduct = redmiproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()

    return redirect(reverse('RedmiApp:redmicategories'))


def redmiremoveitemcart(request, id):
    r = RedmiCartItem.objects.filter(id = id, user = request.user)
    r.delete()

    return redirect(reverse('APP:viewcart'))


def redmiincrementitem(request , redmiproduct):
    r = RedmiCartItem.objects.get(redmiproduct = redmiproduct, user = request.user)
    r.quantity += 1
    r.save()

    return redirect(reverse('APP:viewcart'))

def redmidecrementitem(request , redmiproduct):
    r = RedmiCartItem.objects.get(redmiproduct = redmiproduct, user = request.user)
    
    if (r.quantity > 1):
        r.quantity -= 1
    r.save()

    return redirect(reverse('APP:viewcart'))


#==============================realme cart==================================

def realmeaddtocartview(request, slug=None, id=None):
    realmeproduct = Realme.objects.get(id=id)
    

    cartitem, created = RealmeCartItem.objects.get_or_create(realmeproduct = realmeproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()

    return redirect(reverse('RealmeApp:realmecategories'))


def realmeremoveitemcart(request, id):
    r = RealmeCartItem.objects.filter(id = id, user = request.user)
    r.delete()

    return redirect(reverse('APP:viewcart'))

def realmeincrementitem(request , realmeproduct):
    r = RealmeCartItem.objects.get(realmeproduct = realmeproduct, user = request.user)
    r.quantity += 1
    r.save()

    return redirect(reverse('APP:viewcart'))

def realmedecrementitem(request , realmeproduct):
    r = RealmeCartItem.objects.get(realmeproduct = realmeproduct, user = request.user)
    
    if (r.quantity > 1):
        r.quantity -= 1
    r.save()

    return redirect(reverse('APP:viewcart'))