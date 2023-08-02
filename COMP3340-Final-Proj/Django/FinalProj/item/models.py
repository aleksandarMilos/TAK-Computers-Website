from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self): #this is to just help with the Appearance of the names in Django administration aka http://127.0.0.1:8000/admin/item/category/
        return self.name



class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images')
    is_sold = models.BooleanField(default=False) #can remove this if we don't want to indicate if things are sold or not
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # <= if the user is deleted, all the items are deleted as well
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #Same thing here http://127.0.0.1:8000/admin/item/item/
        return self.name