from django.utils import timezone
from django.db import models

# Create your models here.

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/') 

class users(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=8)
    phone = models.IntegerField()

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('shopping', 'Shopping'),
        ('family', 'Family'),
        ('hobbies', 'Hobbies'),
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
    ]
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='work')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    reminder_time = models.DateTimeField(null=True, blank=True)  # New field for reminder time


    def __str__(self):
        return f"{self.firstname} {self.lastname}"