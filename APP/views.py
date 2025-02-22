from django.shortcuts import render
from EMOBILESCART import settings
# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import BadHeaderError, send_mail
import random
from django.contrib.auth.hashers import check_password #to check the decrypted password with the newpassword
import requests


#check_password----> to get the decrypted password to check it

# Create your views here.

@login_required(login_url='APP:login')
def HomeView(request):
    data = Trends.objects.all()
    return render(request, 'home.html', {'d':data})

# ######################################     OTP VERIFICATION      ###################################

otp_confirm=None

def ForgotPassWordView(request):
    global otp_confirm
    if request.method == 'POST':
        

        user = User.objects.filter(email = request.POST['email'])

        
        if user.exists():
            
            otp = random.randint(000000, 999999)
            otp_confirm = otp #-------- One time password which will work only one time

            
            subject = 'To Modify Password'
            mesg = f'OTP FOR PASSWORD RESET: {otp_confirm}'

            send_mail(subject=subject, message=mesg, from_email=settings.EMAIL_HOST_USER, recipient_list=[request.POST['email']])
            return redirect(reverse('APP:otp_confirm'))

        else:
            messages.error(request, 'Email was not registered')
            return render(request, 'forgotpassword.html')
            

    return render(request, 'forgotpassword.html')


def OTP_verfication(request):
    if request.method == 'POST':
        otp = request.POST['OTP']

        # print(otp_confirm) #-------- One time password which will work only one time
        
        if str(otp) == str(otp_confirm):
            return redirect(reverse('APP:success'))

        messages.error(request, 'Invaild OTP')


    return render(request, 'otp_verfication.html')


def successView(request):

    if request.method == 'POST':
        email = request.POST['email']
        # print(email)
        # print(type(email))
        newpassword = request.POST['newpassword']
        reenterpassword = request.POST['reenterpassword']

        user = User.objects.filter(email = email)
        # print(user)
        # print()
        # print('*')
        if user:
            if not check_password(newpassword, user[0].password): #checks wheather the newpassword is equal or not eaqual to old password.
                if newpassword == reenterpassword:
                    
                    # print(user[0].password) #pbkdf2_sha256$720000$Z62oBqR6cV0RNOJ9LyxnBA$Vr2IUMNH8STk31Zit2AqKA0vjEQ1nqenkU8Q8Pphsgo=
                    # print(check_password(newpassword, user[0].password)) #False
                    
                    # print(user[0].password) ----> old password haser= pbkdf2_sha256$720000$Z62oBqR6cV0RNOJ9LyxnBA$Vr2IUMNH8STk31Zit2AqKA0vjEQ1nqenkU8Q8Pphsgo=
                    NP = make_password(newpassword)

                    user[0].password = NP

                    # print('*'*10)
                    # print(user[0].password) ---> new hased password = pbkdf2_sha256$720000$z8xG1SUl7DKCLBvg2WLG9j$kjPxwEYLDUr3DzZIbpuNjUmqzoeCIL3MWxykP56Y4x4=
                    
                    user[0].save() #To save the password.

                    # To send the password changed successfully to mail

                    subject = 'Password Changed successfully'
                    meg = f'{user[0].username} your password has been changed successfully'
                    send_mail(subject=subject, message=meg, from_email=settings.EMAIL_HOST_USER, recipient_list=[user[0].email])

                    return redirect(reverse('APP:login'))
            
                else:
                    messages.error(request, 'Password not matched!')
            else:
                messages.error(request, 'Please chose a different password!')
        else:
            messages.error(request, 'Invalid email!')        


    return render(request, 'success.html')


# #########################################################################

def RegisterView(request):
    if request.method == "POST":
        if "send_otp" in request.POST:

            email = request.POST.get("email")

            useremail = User.objects.filter(email=email).exists()

            if useremail:
                return render(request, "register.html", {"error": "This email is already registered. Kindly use another email!"})
            
            
            username = request.POST.get("username")
            firstname = request.POST.get("first_name")
            lastname = request.POST.get("last_name")


            if not email:
                return render(request, "register.html", {"error": "Email is required"})

            otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
            request.session["username"] = username  
            request.session["first_name"] = firstname
            request.session["last_name"] = lastname
            request.session["email_otp"] = otp  # Save OTP in session
            request.session["otp_email"] = email  
            request.session["otp_verified"] = False
            request.session["otp_sent"] = False

            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP is {otp}. Do not share it with anyone.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            request.session["otp_sent"] = True

            return render(request, "register.html", {
                "otp_sent": True, 
                "message": "OTP sent successfully!", 
                "email": email,
                "username": username,
                "firstname": firstname,
                "lastname": lastname
            })

        elif "verify_otp" in request.POST:
            entered_otp = request.POST.get("emailOTP")
            stored_otp = request.session.get("email_otp")

            if not entered_otp:
                return render(request, "register.html", {
                    "error": "Please enter the OTP", 
                    "otp_sent": True,
                    "otp_verified": False,
                    "email": request.session.get("otp_email"),
                    "username": request.session.get("username"),
                    "firstname": request.session.get("first_name"),
                    "lastname": request.session.get("last_name"),
                })

            if str(entered_otp) == str(stored_otp):
                request.session["otp_verified"] = True

                return render(request, "register.html", {
                    "message": "OTP verified successfully!",
                    "otp_sent": False,
                    "otp_verified": True,
                    "email": request.session.get("otp_email"),
                    "username": request.session.get("username"),
                    "firstname": request.session.get("first_name"),
                    "lastname": request.session.get("last_name"),
                })
            else:
                return render(request, "register.html", {
                    "error": "Invalid OTP",
                    "otp_sent": True,
                    "otp_verified": False,
                    "email": request.session.get("otp_email"),
                    "username": request.session.get("username"),
                    "firstname": request.session.get("first_name"),
                    "lastname": request.session.get("last_name"),
                })
            
        else:
            request.session["username"] = request.POST.get("username") 
            request.session["first_name"] = request.POST.get("first_name")
            request.session["last_name"] = request.POST.get("last_name")
            request.session["otp_email"] = request.POST.get("email")

            if not request.session.get("otp_sent"):
                return render(request, "register.html", {
                    "error": "Please verify your email before registering.",
                    "otp_sent": False,
                    "otp_verified": False,
                    "email": request.session.get("otp_email"),
                    "username": request.session.get("username"),
                    "firstname": request.session.get("first_name"),
                    "lastname": request.session.get("last_name"),
                })

            if not request.session.get("otp_verified"):  # Ensure OTP was verified
                return render(request, "register.html", {
                    "error": "Please verify your OTP before registering.",
                    "otp_sent": True,
                    "otp_verified": False,
                    "email": request.session.get("otp_email"),
                    "username": request.session.get("username"),
                    "firstname": request.session.get("first_name"),
                    "lastname": request.session.get("last_name"),
                })
            
            user = User.objects.filter(username = request.POST['username'])
            if user.exists():
                messages.info(request, 'user already exist')
                return redirect(reverse('APP:register'))
                
            form = Register(request.POST)
            if form.is_valid():
                form.save()
    
                u = form.cleaned_data['username']
                email = form.cleaned_data['email']
                subject = 'Registered Successfully for E-MobileCart'
                msg = f'Hi {u} , your Account has been created for E-MOBILECART. Enjoy Shopping'

                send_mail(subject=subject, message=msg, from_email=settings.EMAIL_HOST_USER, recipient_list=[email] )

                request.session["first_name"] = ""
                request.session["last_name"] = ""
                request.session["username"] = ""
                request.session["otp_verified"] = False
                request.session["otp_sent"] = False

                return redirect(reverse('APP:login'))
                
            form = Register()
            return render(request, 'register.html', {'f':form})

    return render(request, "register.html", {
        "email": request.session.get("otp_email", ""),
        "username": request.session.get("username", ""),
        "firstname": request.session.get("first_name", ""),
        "lastname": request.session.get("last_name", "")
    })


def CusLoginView(request):
    if request.method == 'POST':
        f = Login(request.POST)
        if f.is_valid():
            user = authenticate(username = f.cleaned_data['username'], password = f.cleaned_data['password'])
            
            u = f.cleaned_data['username']
            subject = 'Logined successfully'
            mesg = f'Nice to see you {u}.'
            
            if user:
                login(request, user)
                
                request.session["otp_email"] = user.email

                send_mail(subject=subject, message=mesg, from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email])
                data = Trends.objects.all()

                return render(request, 'home.html', {'u':user, 'd':data})
            else:
                messages.info(request, 'invalid username or password')
                return redirect(reverse('APP:login'))
            
    f = Login()
    return render(request, 'login.html', {'f':f})

def UserView(request):
    return render(request, 'user.html')

def CusLogoutView(request):
    logout(request)
    request.session["otp_email"] = ""
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
    # print(request.POST)

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

    originalUserEmail = request.session["otp_email"]
    if request.method == 'POST':
        
        user = User.objects.filter(email= originalUserEmail)

        # print(user[0].email)
        if user.exists():
            mobile = request.POST['PhNo']
            pincode = request.POST['PinCode']

            paymentMode = request.POST['PaymentMode']
            
            if len(mobile) == 10 and len(pincode) == 6:

                apiKey = "a9e82866c40974c297c09a6edb4b22a7"

                apiURL = f'http://apilayer.net/api/validate?access_key={apiKey}&number={mobile}&country_code=IN&format=1'

                try:
                    response = requests.get(apiURL)
                    data = response.json()
                    print(data)
                    if data['valid'] == True:
                        pass
                    else:
                        return render(request, 'cart.html', {'error': 'Invalid Mobile No!', 'originalUserEmail': originalUserEmail})
                except requests.exceptions.RequestException:
                    return False

                try:
                    response = requests.get(f'https://api.postalpincode.in/pincode/{pincode}')
                    data = response.json()
                    print(data)
                    if data[0]['Status'] == 'Success':
                        pass
                    else:
                        return render(request, 'cart.html', {'error': 'Invalid Pin!', 'originalUserEmail': originalUserEmail})
                except requests.exceptions.RequestException:
                    return False

                
                applecartdata = CartItem.objects.all()
                onepluscartdata = OneplusCartItem.objects.all()
                realmecartdata = RealmeCartItem.objects.all()
                readmicartdata = RedmiCartItem.objects.all()
                samsungcartdata = SamsungCartItem.objects.all()

                subject = 'Your order are placed successfully'
                
                applemess = []
                oneplusmess = []
                realmemess = []
                readmimes = []
                samsungmess = []


                for i1 in range(len(applecartdata)):
                        applemess += f'apple mobile {i1+1} : {applecartdata[i1].appleproduct} * {applecartdata[i1].quantity} \n'
                
                for i2 in range(len(onepluscartdata)):
                        oneplusmess += f'oneplus mobile {i2+1} : {onepluscartdata[i2].oneplusproduct} * {onepluscartdata[i2].quantity} \n'

                for i3 in range(len(realmecartdata)):
                        realmemess += f'realme mobile {i3+1} : {realmecartdata[i3].realmeproduct} * {realmecartdata[i3].quantity} \n'
                    
                for i4 in range(len(readmicartdata)):
                        readmimes +=  f'redmi mobile {i4+1} : {readmicartdata[i4].redmiproduct} * {readmicartdata[i4].quantity} \n'
                    
                for i5 in range(len(samsungcartdata)):
                        samsungmess += f'samsung mobile {i5+1} : {samsungcartdata[i5].samsungproduct} * {samsungcartdata[i5].quantity} \n'  

                
                
                apples_res = filter((lambda i :i if len(i)!=0 else ''), applemess)
                oneplus_res = filter((lambda i :i if len(i)!=0 else ''), oneplusmess)
                realme_res = filter((lambda i :i if len(i)!=0 else ''), realmemess)
                readmi_res = filter((lambda i :i if len(i)!=0 else ''), readmimes)
                samsung_res = filter((lambda i :i if len(i)!=0 else ''), samsungmess)

                if totalprize > 0:

                    mess = ''.join(list(apples_res)) + '' + ''.join(list(oneplus_res)) + '' + ''.join(list(realme_res)) + '' + ''.join(list(readmi_res)) + '' + ''.join(list(samsung_res)) + '\n Total ammount: ' + str(totalprize) + '-/Rs'

                    send_mail(subject=subject, message=mess, from_email=settings.EMAIL_HOST_USER, recipient_list=[user[0].email])
                    
                    for j in (applecartdata, onepluscartdata, realmecartdata, readmicartdata, samsungcartdata):
                        for i in j:
                            i.delete()

                    return redirect(reverse('APP:successpage'))
                
                else:
                    messages.error(request, 'Your cart is empty!')
            else:
                messages.error(request, 'Please check the mobile no and pincode!')

        else:
            messages.error(request, 'The email is not registered!')        
                
                
                

    return render(request, 'cart.html', {'cartitems':cartitems, 'onepluscartitem':onepluscartitem, 'samsungcartitem':samsungcartitem, 'redmicartitem':redmicartitem, 'realmecartitem':realmecartitem, 'appletotalprize':applesum, 'oneplustotalprize':oneplussum, 'samsungtotalprize':samsungsum, 'redmitotalprize':redmisum, 'realmetotalprize':realmesum, 'totalprize':totalprize, 'originalUserEmail': originalUserEmail})
   

@login_required(login_url='APP:login')
def successpageview(request):
    return render(request, 'successpage.html')

#==============================apple cart==================================
def addtocartview(request, slug=None, id=None):
    appleproduct = Apple.objects.get(id=id)
    
    cartitem, created = CartItem.objects.get_or_create(appleproduct = appleproduct, user = request.user)
    cartitem.quantity += 1
    cartitem.save()
    
    messages.success(request, 'Item added successfully')

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

    messages.success(request, 'Item added successfully')
    
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

    messages.success(request, 'Item added successfully')

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

    messages.success(request, 'Item added successfully')

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

    messages.success(request, 'Item added successfully')

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