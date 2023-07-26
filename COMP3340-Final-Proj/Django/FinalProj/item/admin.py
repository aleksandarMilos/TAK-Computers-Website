from django.contrib import admin

# Register your models here.
from .models import Category, Item #.models because models is in same file as admin

admin.site.register(Category)
admin.site.register(Item)