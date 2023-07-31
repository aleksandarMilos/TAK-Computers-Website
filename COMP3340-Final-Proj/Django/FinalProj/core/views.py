from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from item.models import Category, Item
from django.contrib import messages

from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm #this is from the forms.py SignupForm we created

# Creating our first view
def index(request):
    items = Item.objects.filter(is_sold=False)[0:9] #Obviously adjust this if we're not using the is_sold thing
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST': #we know then that the form has been submitted
        form = SignupForm(request.POST) #gets all the information from the form

        if form.is_valid():
            form.save() #saves user into database

            return redirect('/login/')
    
    else:
        form = SignupForm()
    return render(request, 'core/signup.html',{
        'form': form
    })

def logout_user(request):
    logout(request)
    messages.success(request, ("You were successfully logged out!"))
    return redirect('/')

@login_required
def profile(request):
    return render(request, 'core/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile/')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'core/profile_update.html', context)