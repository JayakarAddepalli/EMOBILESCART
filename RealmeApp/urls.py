from django.urls import path
from .views import *

app_name = 'RealmeApp'

urlpatterns =[
    path('categories/realme/', RealmeCategoriesView, name='realmecategories'),
    path('categories/realme/<slug>/', RealmeCategoriesViewItem , name='realmepro')

]