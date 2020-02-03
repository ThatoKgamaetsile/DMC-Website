from django.db import models

class ContactForm(models.Model):

    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Message = models.CharField(max_length=200)


