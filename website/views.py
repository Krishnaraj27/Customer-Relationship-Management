from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()

    if request.method == 'POST' :
        uname = request.POST['uname']
        upass = request.POST['upassword']
        #authenticate
        user = authenticate(request, username=uname, password=upass)
        if user is not None :
            login(request, user)
            messages.success(request, "You have been logged in successfully !!")
            return redirect('home')
        else : 
            messages.success(request, 'Sorry there was an error while logging in. Please try again...')
    return render(request, 'home.html',{'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out !!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password1']
            user = authenticate(username=uname,password=upass)
            login(request, user)
            messages.success(request, "You have been registered successfully... Welcome to home page !!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
     
    return render(request, 'register.html',{'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        cust_record = Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':cust_record})   
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_rec = Record.objects.get(id=pk)
        delete_rec.delete()
        messages.success(request, "Record deleted Succeddfully...")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete a record...")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added successfully...")
                return redirect('home')
        return render(request, 'add_record.html',{'form':form})
    else:
        messages.success(request, 'You must be logged in to add record...')
        return redirect('home')

def edit_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated!')
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
        messages.success(request, 'You must be logged in to update a record...')
        return redirect('home')