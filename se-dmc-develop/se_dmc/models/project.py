from django.db import models


class Project(models.Model):
    
    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    duration = models.DecimalField(verbose_name='Project duration', decimal_places=2, max_digits=2)
    active = models.BooleanField(default=False, verbose_name='Is project ative')