from Flights import *
from Passengers import *
from datetime import datetime
import numpy as np
class InformationSystem():
    
    def __init__(self, flights):
        self.flights = flights
        #self.passengers = passengers
        #self.gates = []
        
    def getFlights(self):
        flightsData = np.array(self.flights.getFlightsData())[:,0:-1]
       

        return flightsData       
    # def getPassengers(self):
    #     passengersData = self.passengers.getPassengersList()

  
  
  
    def showFlightInformation(self, flightName):
        for flight in self.getFlights():
            print(flight[0],flightName ,flight[0] == flightName )
            if flight[0] == flightName:
                print(
                    f"Lot {flight[0]} do {flight[3]} odlatuje z bramki {flight[4]} o godzinie {flight[1]}\n \
                    Lot będzie trwał {flight[2] - flight[1]}"
                      )
                return f"Lot {flight[0]} do {flight[3]} odlatuje z bramki {flight[4]} o godzinie {flight[1]}\nLot będzie trwał {flight[2] - flight[1]}"
                      
        return f"Nie znaleziono lotu {flightName}"
            
            #print(flight)
        
        
        
        ...
        
if __name__ == '__main__':
    


    loty = Flights()
    loty.AddFlightsFromDatabase()
    info = InformationSystem(loty)
    print(info.getFlights())
    print(info.showFlightInformation('RY9999'))


