from django.shortcuts import render

from distutils.log import error
import email 
from re import S
from urllib import request
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from home.models import Register,Contacts

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def language(request):
    return render(request,'language.html')

def communication(request):
    return render(request,'communication.html')

def business(request):
    return render(request,'business.html')

def software(request):
    return render(request,'software.html')

def social_media(request):
    return render(request,'social_media.html')

def photography(request):
    return render(request,'photography.html')

def course_details(request):
    return render(request,'course_details.html')

def coming_soon(request):
    return render(request,'coming_soon.html')

def blog(request):
    return render(request,'blog.html')

def form(request):
    return render(request,'form.html')

def faq(request):
    return render(request,'faq.html')

def gallery(request):
    return render(request,'gallery.html')

# def contact(request):
#     return render(request,'contact.html')

def contact(request):
    if request.method =='POST':
        Full_Name = request.POST.get('Full_Name')
        Subject = request.POST.get('Subject')
        Mobile = request.POST.get('Mobile')
        Email = request.POST.get('Email')
        Message = request.POST.get('Message')
        
        Contact = Contacts(Full_Name = Full_Name, Subject = Subject, Mobile = Mobile,
                           Email = Email, Message = Message)
        
        Contact.save()
        return redirect('/')
    else:
        return render(request,'contact.html')

# def register(request):
#     return render(request,'register.html')

def register(request):
    if request.method =='POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Confirm_Password = request.POST.get('Confirm_Password')
        
        Studentregister = Register(Name = Name, Email = Email, Password = Password, Confirm_Password = Confirm_Password)
        
        Studentregister.save()
        user = User.objects.create_user(Email,Email, Password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            return redirect('/login')
    else:
         return render(request,'login.html')

