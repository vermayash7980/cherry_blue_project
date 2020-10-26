from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path ('',views.index,name='home'),
    path ("contactus",views.contactus,name='contactus'),
    path ("admit",views.admit,name = 'Admit new patient'),
    path ("meeting",views.meeting,name = 'Meeting the doctor'),
    path ("checkout",views.checkout,name = 'checkout'),
    path ("adminlogin",views.adminlogin,name='adminlogin'),
    path ("aboutus",views.aboutus,name='aboutus')

]
