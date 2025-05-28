from django.db import models

# Create your models here.
class Avenger(models.Model):
    name= models.CharField(max_length=50)
    heroic_name= models.CharField(max_length=50)