from django.db import models

class Flight(models.Model):
   TYPE_CHOICES = [
       ('Nacional', 'Nacional'),
       ('Internacional', 'Internacional'),
   ]

   name = models.CharField(max_length=255)
   flight_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
   price = models.DecimalField(max_digits=10, decimal_places=2)

   def __str__(self):
       return self.name