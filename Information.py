from Flights import *
from Passengers import *
from pprint import pprint
from datetime import datetime
import numpy as np
class InformationSystem():
    
    def __init__(self, flights):
        self.flights = flights
        #self.passengers = passengers
        #self.gates = []
        
    def getFlights(self):
        flightsData = np.array(self.flights.getFlightsData())[:,0:-1]
       
        #pprint(flightsData) 
        return flightsData       
    # def getPassengers(self):
    #     passengersData = self.passengers.getPassengersList()
    #     pprint(passengersData)
  
  
  
    def showFlightInformation(self, flightName):
        for flight in self.getFlights():
            if flight[0] == flightName:
                # print(
                #     f"Lot {flight[0]} do {flight[3]} odlatuje z bramki {flight[4]} o godzinie {flight[1]}\n \
                #     Lot będzie trwał {flight[2] - flight[1]}"
                #       )
                return f"Lot {flight[0]} do {flight[3]} odlatuje z bramki {flight[4]} o godzinie {flight[1]}\nLot będzie trwał {flight[2] - flight[1]}"
                      
            
            
            #print(flight)
        
        
        
        ...
        
if __name__ == '__main__':
    


    loty = Flights()
    loty.AddFlightsFromDatabase()
    info = InformationSystem(loty)
    print(info.getFlights())
    print(info.showFlightInformation('RY9999'))


