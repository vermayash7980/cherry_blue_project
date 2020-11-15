from django.contrib import admin
from django.urls import path ,include
from staff import views

urlpatterns = [
    path ("",views.staff_index,name='staff_index'),
    path ("admit",views.admit,name = 'Admit new patient'),
    path ("admit2",views.admit2,name = 'on admit button pressed'),
    path ("checkout/<int:id>/",views.checkout,name = 'checkout'),
    path ("stafflogin",views.stafflogin,name='stafflogin'),
    path ("stafflogout",views.stafflogout,name='stafflogout')

]
