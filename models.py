from django.db import models

# Create your models here.

class registertable(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=8)
