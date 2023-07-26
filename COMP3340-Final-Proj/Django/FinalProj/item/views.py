from django.shortcuts import render, get_object_or_404

from .models import Item

# Create your views here.

# This view is for creating the details page for the item
def detail(request, pk): #pk stands for primary key
    item = get_object_or_404(Item, pk=pk) #Get the object, or get 404 error
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3] #this is for displaying related items in the same category

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })