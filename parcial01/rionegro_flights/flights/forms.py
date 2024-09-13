from django import forms
from flights.models import Flight

class FlightForm(forms.ModelForm):
   class Meta:
       model = Flight
       fields = ['name', 'flight_type', 'price']

