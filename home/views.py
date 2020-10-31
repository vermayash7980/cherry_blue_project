from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index (request):
    return render(request, 'index.html')

def contactus (request):
    if (request.method =="POST") :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(
            name=name,
            email=email,
            phone=phone,
            desc=desc,
            date=datetime.today()
            )
        contact.save()
        messages.success(request, ' THANK YOU! Your information is received')
    return render(request, 'contactus.html')

def aboutus (request):
    return render(request,'aboutus.html')

