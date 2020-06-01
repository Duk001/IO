from Flights import *
from Passengers import *

from Test import *

class AirportControl():
    def __init__(self, flights, passengers):
        self.flights = flights
        #self.passengers = passengers
        self.sensors = []
        
    def addFlight(self):
        ...