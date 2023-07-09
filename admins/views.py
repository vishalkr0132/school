from urllib import request
from django.shortcuts import render
from requests import request
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from home.models import Contacts
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
         return render(request,'admins/index.html')

def gallery(request):
    return render(request,'admins/gallery.html')

def Add_image(request):
    return render(request,'admins/Add_image.html')

# def Contact(request):
#     return render(request,'admins/Contact.html')

def Contact(request):
    contactlist = Contacts.objects.all()
    c = {'contactlist':contactlist}
    return render(request,'admins/Contact.html',c)

def graphs(request):
    return render(request,'admins/graphs.html')

def inbox(request):
    return render(request,'admins/inbox.html')

def layout(request):
    return render(request,'admins/layout.html')

def logoutuser(request):
    logout(request)
    return redirect('login')
