from unicodedata import decimal
from django.db import models

# Create your models here.
class Student(models.Model):
    seatNumber = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=100)
    arabic = models.DecimalField( max_digits=4, decimal_places=1)
    math = models.DecimalField(max_digits=4, decimal_places=1)
    english = models.DecimalField(max_digits=4, decimal_places=1)
    social = models.DecimalField(max_digits=4, decimal_places=1)
    sience = models.DecimalField(max_digits=4, decimal_places=1)
    islamic= models.DecimalField(max_digits=4, decimal_places=1)
    olenglish = models.DecimalField(max_digits=4, decimal_places=1)
    computer = models.DecimalField(max_digits=4, decimal_places=1)
    art = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.name
     

class Student2(models.Model):
    seatNumber = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=100)
    arabic = models.DecimalField( max_digits=4, decimal_places=1)
    math = models.DecimalField(max_digits=4, decimal_places=1)
    english = models.DecimalField(max_digits=4, decimal_places=1)
    social = models.DecimalField(max_digits=4, decimal_places=1)
    sience = models.DecimalField(max_digits=4, decimal_places=1)
    islamic= models.DecimalField(max_digits=4, decimal_places=1)
    olenglish = models.DecimalField(max_digits=4, decimal_places=1)
    computer = models.DecimalField(max_digits=4, decimal_places=1)
    art = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.name
    
