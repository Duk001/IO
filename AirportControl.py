from Flights import *
from Passengers import *
import Add_to_database_AND_SELECT as db
from datetime import datetime
from datetime import timedelta  
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
            self.flights.AddFlightsFromDatabase()
            return
        print('Wybrany bilet jest już w użyciu')    
        
            
            
            
    def DelayControl(self,flightName, Delay):
        border = timedelta(minutes = 30)
        for flight in self.flights.flights:
            if flightName == flight.getName():
                delayedFlight = flight
                break
            
            
        
        
        DelayedDeparture = delayedFlight.getDeparture() + timedelta(minutes = Delay)
        DelayedArrival = delayedFlight.getArrival() + timedelta(minutes = Delay)
        FlightTime = DelayedArrival - DelayedDeparture
        
        folowingFlights = []
        for flight in self.flights.flights:
            if flightName != flight.getName():
                if flight.getDeparture() >= DelayedDeparture:
                    #print('Lot w pętli: ',flight.getDeparture())
                    TimeDelta = flight.getDeparture() - DelayedDeparture
                    folowingFlights.append(flight.getDeparture())
                    #print(f"Time Delta: {TimeDelta}")
                
        #print(folowingFlights)
        
        for elem in folowingFlights:
            #print(elem - DelayedDeparture)
            if elem - DelayedDeparture <= border:
                DelayedDeparture = border/2 + elem
                DelayedArrival = border/2 + elem + FlightTime
                break

        DelayedDeparture = DelayedDeparture.strftime("%d/%m/%y %H:%M:%S")
        DelayedArrival = DelayedArrival.strftime("%d/%m/%y %H:%M:%S")
        
        #print(DelayedDeparture,DelayedArrival)
        sql = f"UPDATE `lot` SET `Godzina_odlotu` = '{DelayedDeparture}', `Godzina_przylotu` = '{DelayedArrival}' WHERE `lot`.`Nazwa_lotu` = '{str(flightName).strip()}';"
        #print(sql)
        db.dodaj(sql)
        return DelayedDeparture,DelayedArrival
        

        
if __name__ == '__main__':
    Flights = Flights()
    Flights.AddFlightsFromDatabase() 
    AirportControl = AirportControl(Flights)
    
    
    AirportControl.DelayControl('RY1082',20)
        
        
    
    
    
    
    
    # #AirportControl.addFlight('Test','T222','Tuploev tu140','23/7/20 12:00:00','23/7/20 16:00:00','A10','Moskwa')
    #AirportControl.addPassenger(311,'Michał','Nowak','Test','podręczny','Waiting for checkin',21)
    # print
    
    # ListOfTicketsInUse = [elem[0] for elem in db.getPassengersFromDatabase()]
    # print(ListOfTicketsInUse)
    
    
#'312','Adam','Nowak','Test','podręczny','Waiting for checkin',21