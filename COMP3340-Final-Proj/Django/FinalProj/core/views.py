from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm #this is from the forms.py SignupForm we created

# Creating our first view
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6] #Obviously adjust this if we're not using the is_sold thing
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

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