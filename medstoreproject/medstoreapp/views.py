from django.shortcuts import render,redirect
from .models import storeModel
from .forms import storeForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test

def signup(request):
    if request.method=='POST':
         form=UserCreationForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('login')
    form=UserCreationForm()
    return render(request,'signup.html',{'form':form})

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