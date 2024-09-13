from flights.models import Flight
from django.db.models import Avg

class FlightRepository: 
    def __init__(self) -> None:
        self.model = Flight

    def get_all_flights(self):
        return self.model.objects.all().order_by('price')

    def create_flight(self, data):
        return self.model.objects.create(**data)

    def get_flight_by_id(self, flight_id):
        return self.model.objects.get(id=flight_id)

    def count_flights_by_type(self, flight_type):
        return self.model.objects.filter(flight_type=flight_type).count()
    
    def get_average_price_by_type(self, flight_type):
        return self.model.objects.filter(flight_type=flight_type).aggregate(Avg('price'))['price__avg'] or 0
