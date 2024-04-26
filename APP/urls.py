from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'APP'

urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', CusLoginView, name='login'),
    path('user/', UserView, name='user'),
    path('logout/', CusLogoutView, name='logout'),
    path('cart/', viewcart, name='viewcart'),
    path('checkpayment/', successviewcheck, name='paymentsuccessfull'),
    path('successpage/', successpageview, name='successpage'),

    path('forgotpassword/', ForgotPassWordView, name='Forgotpassword'),
    path('otp_confirm/', OTP_verfication, name='otp_confirm'),
    path('success/',successView, name='success'),

    
    path('buynow/<int:id>',APPLEBUYNOWVIEW, name='buynow'),
    path('addtocart/<slug>/<int:id>', addtocartview, name='addtocart'),
    path('removeitemcart/<int:id>', removeitemcart, name='removeitemcart'),
    path('increment/<appleproduct>/', incrementitem , name = 'increment'),
    path('decrement/<appleproduct>/', decrementitem , name = 'decrement'),

    path('oneplusbuynow/<int:id>',ONEPLUSBUYNOWVIEW, name='oneplusbuynow'),
    path('oneplusaddtocart/<slug>/<int:id>', oneplusaddtocartview, name='oneplusaddtocart'),
    path('oneplusremoveitemcart/<int:id>', oneplusremoveitemcart, name='oneplusremoveitemcart'),
    path('oneplusincrement/<oneplusproduct>/', oneplusincrementitem , name = 'oneplusincrement'),
    path('oneplusdecrement/<oneplusproduct>/', oneplusdecrementitem , name = 'oneplusdecrement'),

    path('samsungbuynow/<int:id>',SAMSUNGBUYNOWVIEW, name='samsungbuynow'),
    path('samsungaddtocart/<slug>/<int:id>', samsungaddtocartview, name='samsungaddtocart'),
    path('samsungremoveitemcart/<int:id>', samsungremoveitemcart, name='samsungremoveitemcart'),
    path('samsungincrement/<samsungproduct>/', samsungincrementitem , name = 'samsungincrement'),
    path('samsungdecrement/<samsungproduct>/', samsungdecrementitem , name = 'samsungdecrement'),

    path('redmibuynow/<int:id>',REDMIBUYNOWVIEW, name='redmibuynow'),
    path('redmiaddtocart/<slug>/<int:id>', redmiaddtocartview, name='redmiaddtocart'),
    path('redmiremoveitemcart/<int:id>', redmiremoveitemcart, name='redmiremoveitemcart'),
    path('redmiincrement/<redmiproduct>/', redmiincrementitem , name = 'redmiincrement'),
    path('redmidecrement/<redmiproduct>/', redmidecrementitem , name = 'redmidecrement'),

    path('realmebuynow/<int:id>',REALMEBUYNOWVIEW, name='realmebuynow'),
    path('realmeaddtocart/<slug>/<int:id>', realmeaddtocartview, name='realmeaddtocart'),
    path('realmeremoveitemcart/<int:id>', realmeremoveitemcart, name='realmeremoveitemcart'),
    path('realmeincrement/<realmeproduct>/', realmeincrementitem , name = 'realmeincrement'),
    path('realmedecrement/<realmeproduct>/', realmedecrementitem , name = 'realmedecrement'),
]



