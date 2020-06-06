from Flight import *
import Passengers
import Passenger
from datetime import datetime
import Add_to_database_AND_SELECT as db
from copy import deepcopy


pas1 = Passenger.Passenger('Adam Nowak','AF7777',True,'Checked in','JK0001')
pas2 = Passenger.Passenger('Jan Nowak','AF7777',True,'Checked in','JK0002')
tmpPas = Passengers.Passengers([pas1,pas2])


class Flights():
    def __init__(self):     #, flights):
        self.flights = []   #flights
        
        
    def AddFlightsFromDatabase(self):
        self.flights = []
        flightsDB = db.getFlightsFromDatabase()
        passengers = db.getPassengersListFromDatabase()
        passengers = [elem for elem in passengers if elem ] 
        #print(passengers)
        

        
        size  = len(flightsDB)
        
        
        
        #passengerClass = 'None'
        for flightDATA in flightsDB:
            passengerClassList = []
            for elem in db.getPassengersFromFlightFromDatabase(flightDATA[0]):
            #    print(elem)
                passengerClassList.append(
                    Passenger.Passenger(elem[1]+ ' ' + elem[2],elem[3],elem[4],elem[5],elem[0]))
           # print('***')    
            #print(passengerClassList)
            self.flights.append(Flight(flightDATA[0], flightDATA[3],flightDATA[4],flightDATA[6], flightDATA[5],deepcopy(passengerClassList)))
            
            #print(flightDATA[0], flightDATA[3],flightDATA[4],flightDATA[6], flightDATA[5])
            
            # print('*****')
            # print(db.getPassengersFromFlightFromDatabase(flightDATA[0]))

        

            
        
        
        #### TEST:
        #print('Flights: ',flightsDB)
        #print('size: ',size)
        ...
        
        
    def addFlight(self,flight):
        self.flights.append(flight)
        
        
    def removeFlight(self, name):
        for flight in self.flights:
            print(flight.getName())
            if flight.getName() == name:
                self.flights.remove(flight)
                break
    def getFlightsData(self):
        # for flight in self.flights:
        return [flight.getAllData() for flight in self.flights]
    
    def getNamesOfFlights(self):
        return [elem[0] for elem in self.getFlightsData()]
        
    
    

    def getPassengersFromFlight(self, flightName):
        for flight in self.flights:
            if flight.getName() == flightName:
                passengers =flight.getPassengers()
                
               # print(passengers)
                
                for passenger in passengers:
                    print(passenger.getAllData())
                return passengers
                
        else:
            print(f"Nie znaleziono lotu: {flightName}")
            return f"Nie znaleziono lotu: {flightName}"
            




from pprint import pprint




if __name__ == '__main__':
    

    loty = Flights()
    loty.AddFlightsFromDatabase()
 
    
    #loty.getPassengersFromFlight('RY1082')
    loty.getNamesOfFlights()
    
