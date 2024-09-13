from django.views.generic import TemplateView, CreateView, ListView
from django.views import View
from django.urls import reverse_lazy
from flights.forms import FlightForm
from django.shortcuts import render, redirect
from flights.services import FlightService
from django.contrib import messages

class HomeView(TemplateView):
   template_name = 'flights/home.html'
   
class FlightCreateView(View):
    form_class = FlightForm
    template_name = 'flights/register_flight.html'
    success_url = reverse_lazy('list_flights')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            flights_service = FlightService()
            flights_service.register_flight(form.cleaned_data)
            
            messages.success(request, 'El vuelo ha sido registrado exitosamente.')
            return redirect(self.success_url)
        
        return render(request, self.template_name, {'form': form})

class FlightListView(ListView):
   template_name = 'flights/list_flights.html'
   context_object_name = 'flights'

   def get_queryset(self):
       flights_service = FlightService()
       return flights_service.get_flights_list()
   
class FlightStatsView(TemplateView):
   template_name = 'flights/flight_stats.html'

   def get_context_data(self, **kwargs):
       flights_service = FlightService()
       context = super().get_context_data(**kwargs)
       context.update(flights_service.get_flight_statistics())
       return context