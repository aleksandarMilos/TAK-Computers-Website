from django.shortcuts import render

from item.models import Category, Item

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