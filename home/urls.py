from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path ('',views.index,name='home'),
    path ("contactus",views.contactus,name='contactus'),
    path ("aboutus",views.aboutus,name='aboutus')
]
