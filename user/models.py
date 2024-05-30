from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class User(models.Model):
    index = models.IntegerField()
    PID = models.CharField(max_length=20)
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Age = models.IntegerField(
            validators=[MinValueValidator(15),
            MaxValueValidator(120)]
    )
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()