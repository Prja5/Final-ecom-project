from django.db import models

# Create your models here.
class stud(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    msg=models.CharField(max_length=50)

    # create 
    
