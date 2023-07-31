from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'e.g., JohnDoe',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'e.g., johndoe@gmail.com',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
        
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-3 px-4 rounded-xl mb-2'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'e.g., johndoe@gmail.com',
        'class': 'w-full py-3 px-6 rounded-xl mb-2'
    }))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']

    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-3 px-4 rounded-xl mb-2'
    }))

    phone = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'w-full py-3 px-6 rounded-xl mb-2'
    }))
