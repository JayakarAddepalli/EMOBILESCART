from django.urls import path
from .views import *

app_name = 'RedmiApp'

urlpatterns =[
        path('categories/redmi/', RedmiCategoriesView, name='redmicategories'),
        path('categories/redmi/<slug>/', RedmiCategoriesViewItem , name='redmipro'),

]