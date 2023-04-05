from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    class Meta(object):
        db_table = 'about'
# Create your models here.
    name = models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True, default='Anonymous'
    )
    body = models.TextField(
        'Body', blank=False, null=False, db_index=True
    )
    image = CloudinaryField(
        'image', blank=True, null=True
    )