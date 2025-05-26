from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator,RegexValidator,EmailValidator

class database(models.Model):
    name = models.CharField(max_length=15,validators=[RegexValidator(regex='^[A-Za-z]+$',message='Name must contain only letters.')])
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(99)])
    email = models.EmailField()
    phone = models.CharField(max_length=10,validators=[RegexValidator(regex='^\d{10}$',message='Phone number must be exactly 10 digits.')])
    place = models.CharField(max_length=50,error_messages="The place field contain only letter")
