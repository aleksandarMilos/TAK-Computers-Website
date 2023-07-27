from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm
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


#Making it a requirement that we have to be logged in first, in order to add items, if not logged in and we try to add an item, redirected to login page instead
@login_required
def new(request):
    if request.method == 'POST': #this is if the form is submitted
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else: #Aka if its a get request
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item', #for forms.html
    })