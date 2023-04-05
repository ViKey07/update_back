from django.db import models
from cloudinary.models import CloudinaryField


class Item(models.Model):
    STATUS = (
    ('active', 'Active'),
    ('inactive','Inactive'),
    )

    SIZE = (
      
        ('M', 'Medium'),
        ('L', 'Large'),
        
    )

    COLOR = (
        ('red', 'Red'),
        ('White', 'White'),
    )

    STATUS_DICT = dict(STATUS)
    SIZE_DICT = dict(SIZE)
    COLOR_DICT = dict(COLOR)

    class Meta(object):
        db_table = 'items'


    status = models.CharField(
        'status', blank=False, default='inactive', max_length=50, db_index=True, choices=STATUS
    )

    name = models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True, default='name'
    )
    price = models.DecimalField(
        'price', blank=False, null=False, max_digits=14, decimal_places=2
    )
    image = CloudinaryField(
        'image', blank=False, null=False
    )
    size = models.CharField(
        'size', blank=False, null=False, max_length=50, db_index=True, choices=SIZE
    )
    color = models.CharField(
        'color', blank=False, null=False, max_length=50, db_index=True, choices=COLOR
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )

    def __str__(self):
        return self.name