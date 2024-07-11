from django.db import models

# Create your models here.
class users(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=8)
    phone = models.IntegerField()

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"