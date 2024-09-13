from flights.repositories import FlightRepository

class FlightService:
    def __init__(self) -> None:
        self.repository = FlightRepository()

    def register_flight(self, data):
        return self.repository.create_flight(data)

    def get_flights_list(self):
        return self.repository.get_all_flights()

    def get_flight_statistics(self):
        national_count = self.repository.count_flights_by_type('Nacional')
        international_count = self.repository.count_flights_by_type('Internacional')
        national_avg_price = self.repository.get_average_price_by_type('Nacional')
        
        return {
            'national_count': national_count,
            'international_count': international_count,
            'national_avg_price': national_avg_price
        }
