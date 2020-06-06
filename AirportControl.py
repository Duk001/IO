from Flights import *
from Passengers import *
import Add_to_database_AND_SELECT as db

#from Test import *

class AirportControl():
    def __init__(self, flights):
        self.flights = flights
        #self.passengers = passengers
        self.sensors = []
        
    def addFlight(self, Nazwa, Numer_rejerstracyjny, model_samolotu, odlot, przylot, bramka, destynacja):
        self.flights.AddFlightsFromDatabase()
        if Nazwa not in self.flights.getNamesOfFlights():
            db.DodajLot(Nazwa, Numer_rejerstracyjny, model_samolotu, odlot, przylot, bramka, destynacja)
            self.flights.AddFlightsFromDatabase()
            return
        print('Wybrany Lot już istnieje')
        ...
    
    def addPassenger(self,Numer_biletu, Imie, Nazwisko, Nazwa_lotu, typ_bagazu, Status_odprawy, Numer_fotela):
        '''
        # TODO: \n
            @Sprawdzanie czy Pasażer o danym bilecie już istnieje -> inaczej sql się wywali
        
        '''
        ListOfTicketsInUse = [elem[0] for elem in db.getPassengersFromDatabase()]
        
        if Numer_biletu not in ListOfTicketsInUse:
            db.DodajPasazera(Numer_biletu, Imie, Nazwisko, Nazwa_lotu, typ_bagazu, Status_odprawy, Numer_fotela)
            return
        print('Wybrany bilet jest już w użyciu')    
        
            
            
        
        
        self.flights.AddFlightsFromDatabase()
        ...
        
if __name__ == '__main__':
    Flights = Flights()
    Flights.AddFlightsFromDatabase() 
    AirportControl = AirportControl(Flights)
    # #AirportControl.addFlight('Test','T222','Tuploev tu140','23/7/20 12:00:00','23/7/20 16:00:00','A10','Moskwa')
    AirportControl.addPassenger(311,'Michał','Nowak','Test','podręczny','Waiting for checkin',21)
    # print
    
    # ListOfTicketsInUse = [elem[0] for elem in db.getPassengersFromDatabase()]
    # print(ListOfTicketsInUse)
    
    
#'312','Adam','Nowak','Test','podręczny','Waiting for checkin',21