from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',height_field=None, width_field=None, max_length=100)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
@receiver(pre_delete, sender=Item)
def item_pre_delete(sender, instance, **kwargs):
    # Delete the image file from the filesystem
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
