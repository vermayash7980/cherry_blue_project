from django.shortcuts import render,HttpResponse

# Create your views here.
def index (request):
    return render(request, 'index.html')

def contactus (request):
    return render(request, 'contactus.html')

def admit (request):
    return render(request, 'admit.html')
    
def meeting (request):
    return render(request, 'meeting.html')
    
def checkout (request):
    return render(request,'checkout.html')

def adminlogin (request):
    return render(request,'adminlogin.html')

def aboutus (request):
    return render(request,'aboutus.html')