from Flight import *

class Flights():
    def __init__(self, flights):
        self.flights = flights
        
        
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








if __name__ == '__main__':
    lot1 = Flight('abc','19/6/18 13:55:26','19/6/18 16:55:26','Tokyo','A20',['Adam','Ewa','Jan'])
    lot2 = Flight('xyz','19/4/18 13:55:26','19/4/18 19:55:26','Warsaw','A12',['Jakub','Andrzej','Jan'])
    loty = Flights([lot1,lot2])
    lot3 = Flight('123','19/7/19 18:00:26','19/7/19 22:35:26','Madrit','B10',['Michał','Anna','Julia'])
    loty.addFlight(lot3)
    # print(loty.getFlightsData())
    tmp = loty.getFlightsData()
    for elem in tmp:
        print(elem)
    # loty.removeFlight('abc')
    # print(loty.getFlightsData())
    # print(loty.flights)
    
    # tmp = Flight('abc','19/6/18 13:55:26','19/6/18 16:55:26',['Adam','Ewa','Jan'])
    # print(tmp.getPassengers())