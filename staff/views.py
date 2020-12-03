from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from datetime import datetime
from datetime import date as dt
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from staff.models import patient

# Create your views here.
def admit2 (request):
    if (request.user.is_anonymous):
        messages.info(request, 'please login first you cant use this webpage with out login')
        return  redirect('/staff/stafflogin')
    if (request.method == 'POST'):
        name= request.POST.get('first_name')+" "+request.POST.get('last_name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        bg=request.POST.get('bg')
        dept=request.POST.get('dept')
        description=request.POST.get('description')
        y=patient(
            name=name,
            address=address,
            date_of_birth=dob,
            date_of_admit=datetime.today(),
            contact_no=phone,
            blood_grp=bg,
            dept=dept,
            description=description
        )
        y.save()
        messages.success(request, 'Patient admitted successfully')
    return HttpResponseRedirect('/staff/')

def admit(request):
    if (request.user.is_anonymous):
        messages.info(request, 'please login first you cant use this webpage with out login')
        return  redirect('/staff/stafflogin')
    return render(request,'admit.html')
    
def checkout (request, id):
    if (request.user.is_anonymous):
        messages.info(request, 'please login first you cant use this webpage with out login')
        return  redirect('/staff/stafflogin')
    if (request.method == 'POST'):
        x=patient.objects.get(pk=id)
        x.delete()
    return HttpResponseRedirect('/staff/')
    
def staff_index (request):
    if (request.user.is_anonymous):
        messages.info(request, 'please login first you cant use this webpage with out login')
        return  redirect('/staff/stafflogin')
    data = patient.objects.all()
    return render(request,'staff_index.html',{'data':data})

def stafflogout (request):
    logout(request)
    return render(request,'logout.html')

def stafflogin (request):
    if (request.method == "POST"):
        user_name=request.POST.get('user_name')
        password= request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/staff/')
        else:
            # No backend authenticated the credentials
            messages.warning(request, 'please enter the correct credentials')
            return render(request,'stafflogin.html')
    return render(request,'stafflogin.html')

def payment(request ,id):
    if (request.user.is_anonymous):
        messages.info(request, 'please login first you cant use this webpage with out login')
        return  redirect('/staff/stafflogin')
    if (request.method == 'POST'):
        x=patient.objects.get(pk=id)
        y=datetime.now().date()
        delta= str(y-x.date_of_admit)
        return render(request,'payment.html',{'i':x, 'amount' : delta[0:-14]})
    return HttpResponseRedirect('/staff/')