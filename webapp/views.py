from django.shortcuts import render,redirect
from   .forms   import  UserCreationForm,loginUser
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'webapp/index.html')

def about(request):
    return render(request,'webapp/about.html')



# Register
def  Register(request):
    form  = UserCreationForm()
    
    if  request.method=='POST':
        form=UserCreationForm(request.POST)
        
        if  form.is_valid():
            form.save()
            # return redirect('')
            
    context={'form':form}
    return render(request,'webapp/register.html',context=context)
    
# Login
def  Login(request):
    form  = loginUser()
    
    if  request.method=='POST':
        form=loginUser(request.POST)
        
        if  form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if  user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
            
    context={'form':form}
    return render(request,'webapp/login.html',context=context)

# Logout
def  Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
# dashboard
def  Dashboard(request):
    return render(request,'webapp/dashboard.html')

# profile
def  Profile(request):
    return render(request,'webapp/profile.html')

# contact
def  Contact(request):
    return render(request,'webapp/contact.html')

# services
def  Services(request):
    return render(request,'webapp/services.html')

