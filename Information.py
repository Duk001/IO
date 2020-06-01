from Flights import *
from Passengers import *
from pprint import pprint
import numpy as np
class InformationSystem():
    
    def __init__(self, flights, passengers):
        self.flights = flights
        self.passengers = passengers
        self.gates = []
        
    def getFlights(self):
        flightsData = np.array(self.flights.getFlightsData())[:,0:-1]
       
        #pprint(flightsData) 
        return flightsData       
    def getPassengers(self):
        passengersData = self.passengers.getPassengersList()
        pprint(passengersData)
    def showFlightInformation(self, flightName):
        for flight in self.getFlights():
            if flight[0] == flightName:
                print(
                    f"Lot {flight[0]} do {flight[3]} odlatuje z bramki {flight[4]} o godzinie {flight[1]}\n",
                    f"Lot będzie trwał {flight[2] - flight[1]}"
                      )
                return flight
            #print(flight)
        
        
        
        ...
        
if __name__ == '__main__':
    pas1 = Passenger('Adam Nowak','AF777',True,'Checked in','JK0001')
    pas2 = Passenger('Jan Nowak','AF777',True,'Checked in','JK0002')
    pas3 = Passenger('Ewa Kowalska','AF999',False,'Checked in','JK0003')
    pas4 = Passenger('Joanna Duda','AF999',True,'Checked in','JK0004')
    passengers1 = Passengers([pas1,pas2])
    passengers2 = Passengers([pas3,pas4])
    passengersAll = Passengers([pas1,pas2,pas3,pas4])
    lot1 = Flight('AF777','19/6/18 13:55:26','19/6/18 16:55:26','Madry','A20',passengers1)
    lot2 = Flight('AF999','19/4/18 13:55:26','19/4/18 19:55:26','Warsaw','B10',passengers2)
    lotAll = Flights([lot1,lot2])
    
    info = InformationSystem(lotAll,passengersAll)
    #info.getFlights()
    #info.getPassengers()
    info.showFlightInformation('AF777')
    #print(lot1.getAllData())
    