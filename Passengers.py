from Passenger import *

import Add_to_database_AND_SELECT as db
class Passengers():
    def __init__(self, passengers):
        self.passengers = passengers
        
    def addPassenger(self,passenger):
        self.passengers.append(passenger)
    def removePassenger(self,name):
        for passenger in self.passengers:
            print(passenger.getName())
            if passenger.getName() == name:
                self.passengers.remove(passenger)
                break
            
    def updateCheckInStatus(self, name, newStatus):
        for passenger in self.passengers:
            print(passenger.name)
            if passenger.name == name:
                passenger.updateData(name, passenger.flightName, passenger.checkedBaggage,newStatus, passenger.ticket)
                break
    def getPassengersList(self):
        out = [passenger.getAllData() for passenger in self.passengers]
        return out
        #for passenger in self.passengers:
            
        ...
    def getPassengersFromDatabase(self):
        passengersDB = db.getPassengersListFromDatabase()
        
        for passengersDATA in passengersDB:
            for elem in passengersDATA:
                print(elem)
                self.addPassenger(Passenger(elem[1] + ' '+ elem[2], elem[3],elem[4],elem[5],elem[0]))
            #print(passengersDATA)
            
            
        
       # print(passengersDB)
        
        
        


