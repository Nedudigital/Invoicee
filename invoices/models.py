from django.db import models
import datetime
# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField(default='09033873459')
    email = models.EmailField(unique=True)
    date = models.DateField(default=datetime.datetime.now)



class buyer(models.Model): 
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField(default='09033873459')
    email = models.EmailField(unique=True)
    purchase_date = models.DateField(default=datetime.datetime.now)


class product(models.Model):
    image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length= 100)
