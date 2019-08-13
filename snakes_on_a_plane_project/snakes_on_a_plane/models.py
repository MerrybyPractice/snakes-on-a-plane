from django.db import models

# Create your models here.

class Seat(models.Model): 
  seat_number = models.CharField(max_length=200)
  number_of_snakes = models.IntegerField(default=0)

class Snake(models.Model): 
  venemous = models.BooleanField(default=False) 
  house = models.ForeignKey(Seat, on_delete=models.CASCADE)  