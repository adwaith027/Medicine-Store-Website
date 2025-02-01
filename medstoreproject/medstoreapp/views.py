from django.shortcuts import render,redirect
from .models import storeModel
from .forms import storeForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def password_validation(password):
    if len(password)<8:
          return False
    return True

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        uemail=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 != password2:
            messages.error(request,'Passwords do not match')
            return redirect('signup')
        pwd=password2
        if not password_validation(pwd):
            messages.error(request,'Password must be atleast 8 characters long')
            return redirect('signup')
        user=User.objects.create_user(username=uname,email=uemail,password=pwd)
        return redirect('login')
    return render(request,'signup.html')

def userlogin(request):
    if request.method=='POST':
         uname=request.POST.get('username')
         password=request.POST.get('password')
         user=authenticate(username=uname,password=password)
         if user is not None:
              login(request,user)
              return redirect('home')
    return render(request,'login.html')

@login_required(login_url='login')
def userlogout(request):
    if request.method=='POST':
          logout(request)
          return redirect('login')
    user=request.user
    return render(request,'logout.html',{'user':user})

# @login_required(login_url='login')
def home(request):
     return render(request,'home.html')

# @login_required(login_url='login/')
def aboutus(request):
     return render(request,'about.html')

# @login_required(login_url='login')
def create(request):
    form=storeForm()
    if request.method=='POST':
        form=storeForm(request.POST,request.FILES)
        if form.is_valid():
            IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
            tempr=form.save(commit=False)
            tempr.picture=request.FILES['picture']
            ftype=tempr.picture.url.split('.')[-1]
            ftype=ftype.lower()
            if ftype not in IMAGE_FILE_TYPES:
                     return render(request,'create.html',{'form':form,'error':"Image type is not valid"})
            tempr.save()
            
            return redirect('create')
    return render(request,'create.html',{'form':form,"error":""})

def viewall(request):
     medicine=storeModel.objects.all()
     return render(request,'viewall.html',{'medicine':medicine})

def update(request,num):
    medid=storeModel.objects.get(pk=num)
    if request.method=='POST':
        form=storeForm(request.POST,instance=medid)
        if form.is_valid():
            form.save()
            return redirect('viewall')
    else:
        form=storeForm(instance=medid)
    return render(request,'update.html',{'form':form})

def deletemed(request,num):
     medid=storeModel.objects.get(pk=num)
     if request.method=='POST':
          storeModel.delete(medid)
          return redirect('viewall')
     return render(request,'delete.html',{'medid':medid})