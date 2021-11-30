from django.db import models

# Create your models here.

class Userdetails(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(max_length=2)
    email = models.EmailField(max_length=50,default=None)
    contact_number = models.IntegerField(max_length=10,default=0)


