from django.db import models

# Create your models here.

class testDB(models.Model):

    name = models.CharField(max_length=100)
    salary= models.IntegerField()
    age= models.IntegerField()