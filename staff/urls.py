from django.contrib import admin
from django.urls import path ,include
from staff import views

urlpatterns = [
    path ("",views.staff_index,name='staff_index'),
    path ("admit",views.admit,name = 'Admit new patient'),
    path ("meeting",views.meeting,name = 'Meeting the doctor'),
    path ("checkout",views.checkout,name = 'checkout'),
    path ("stafflogin",views.stafflogin,name='stafflogin'),
    path ("stafflogout",views.stafflogout,name='stafflogout')
]
