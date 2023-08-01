from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from item.models import Category, Item
from django.contrib import messages

from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm #this is from the forms.py SignupForm we created
from .models import Profile

from django.core.paginator import Paginator

# Creating our first view
def index(request):
    items = Item.objects.filter(is_sold=False) #Obviously adjust this if we're not using the is_sold thing
    categories = Category.objects.all()

    p = Paginator(items, 6)
    page = request.GET.get('page')
    items_list = p.get_page(page)

    numPages = "a" * items_list.paginator.num_pages

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items_list,
        'numPages': numPages
    })

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def privacy(request):
    return render(request, 'core/privacy.html')


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
    profile, created = Profile.objects.get_or_create(staff=request.user) #fixes and avoids error where profile is not recognized

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