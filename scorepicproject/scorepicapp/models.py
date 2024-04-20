from django.db import models

# Create your models here.

class DataPic(models.Model):
    image = models.ImageField(upload_to = 'images')
    votes = models.IntegerField(default = 0)