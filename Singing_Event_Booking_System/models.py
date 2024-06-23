from django.db import models
from django.contrib.auth.models import AbstractUser

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
from django.db import models


    # Your model fields here

    
    
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.event_name
    




class Booking(models.Model):
    event_name = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return f"Booking ID: {self.id}, Event Name: {self.event_name}"