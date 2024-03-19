from django.urls import path
from .views import *

app_name = 'OneplusAPP'

urlpatterns = [
    path('categories/oneplus/', OneplusCategoriesView, name='Onepluscategories'),
    path('categories/oneplus/<slug>/',OneplusCategoriesViewItem , name='onepluspro'),
]