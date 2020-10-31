from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def admit (request):
    return render(request, 'admit.html')
    
def meeting (request):
    return render(request, 'meeting.html')
    
def checkout (request):
    return render(request,'checkout.html')

def staff_index (request):
    if (request.user.is_anonymous):
        messages.info(request, 'are are bhai kidhar cahle ? pehle log in to kar lo')
        return  redirect('/stafflogin')
    return render(request,'staff.html')

def stafflogout (request):
    logout(request)
    return render(request,'index.html')

def stafflogin (request):
    if (request.method == "POST"):
        user_name=request.POST.get('user_name')
        password= request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/staff')
        else:
            # No backend authenticated the credentials
            messages.warning(request, 'holy shit! how someone can be this much wrong')
            return render(request,'stafflogin.html')
    return render(request,'stafflogin.html')
