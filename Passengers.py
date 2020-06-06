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
        
        
        


if __name__ == '__main__':
    from pprint import pprint
    pas1 = Passenger('Adam Nowak','AF777',True,'Checked in','JK0001')
    pas2 = Passenger('Jan Nowak','AF777',True,'Checked in','JK0002')
    pas3 = Passenger('Ewa Kowalska','AF777',False,'Checked in','JK0003')
    pas4 = Passenger('Joanna Duda','AF777',True,'Checked in','JK0004')
    
    passengers = Passengers([pas4,pas2,pas3,pas1])
    passengers = Passengers([])
    passengers.getPassengersFromDatabase()
    
    pprint(passengers.getPassengersList())
    
    
    # passengers.updateCheckInStatus('Ewa Kowalska', 'Waiting')
    # passengers.removePassenger('Joanna Duda')
    # pprint(passengers.getPassengersList())
    # passengers.addPassenger(pas4)
    # pprint(passengers.getPassengersList())
    
    
    