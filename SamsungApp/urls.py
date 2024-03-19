from django.urls import path
from .views import *

app_name = 'SamsungApp'

urlpatterns =[
    path('categories/samsung/', SamsungCategoriesView, name='samsungcategories'),
    path('categories/samsung/<slug>/', SamsungCategoriesViewItem , name='samsungpro')
]