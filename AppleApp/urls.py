from django.urls import path
from .views import *

app_name = 'AppleApp'

urlpatterns = [
    path('categories/apple/', CategoriesView, name='categories'),
    path('categories/apple/<slug>/', CategoriesViewItem , name='applepro'),
    # path('categories/apple/cartitem/<int:id>/', apple_add_to_cart, name='appleadditem'),
]