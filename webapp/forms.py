from  django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from  django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# create a form for user registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
# create a form for user login
class  loginUser(AuthenticationForm,):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']
        

        
        