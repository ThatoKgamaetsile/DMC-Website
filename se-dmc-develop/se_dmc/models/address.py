from django.db import models


class Address(models.Model):
    
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
