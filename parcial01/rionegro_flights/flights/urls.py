from django.urls import path
from flights.views import HomeView, FlightCreateView, FlightListView, FlightStatsView

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('register/', FlightCreateView.as_view(), name='register_flight'),
   path('list/', FlightListView.as_view(), name='list_flights'),
   path('stats/', FlightStatsView.as_view(), name='flight_stats'),
]