from datetime import datetime
class Flight():
    def __init__(self, name, departure, arrival,destination,gate, passengers):
        '''
      ##  Args: \n
      
            name: nazwa -> string 
            departure: odlot z lotniska -> string w formacie '%d/%m/%y %H:%M:%S' np. ('19/6/18 13:55:26')
            arrival:  przylot na lotnisko docelowe -> format jak wyżej
            passengers:  lista pasażerów -> lista objektów klasy pasażer lub klasa z pasażerami
            
     ##   Returns:\n
            None
            
      ##  Funcs:\n
            @setDeparture(newDeparture)
            @getName()
            @getArrival()
            @getDeparture()
            @getPassengers()
            @getAllData()

        '''
        self.name = name
        self.departure = datetime.strptime(departure, '%d/%m/%y %H:%M:%S') #departure 
        self.arrival =  datetime.strptime(arrival, '%d/%m/%y %H:%M:%S')#arrival
        self.destination = destination
        self.gate = gate
        self.passengers = passengers
    def setDeparture(self,newDeparture):
        '''
        Funkcja zmieniająca datę odlotu i przylotu
        
     ##   Args:
            newDeparture: Nowa data odlotu -> string w formacie '%d/%m/%y %H:%M:%S' np. ('19/6/18 13:55:26')
     ##   Returns:
            None
        '''
        timeDifference = newDeparture - self.departure
        self.departure = newDeparture
        self.arrival += timeDifference
    def getFlightDuration(self):
        return  self.arrival - self.departure
    def getName(self):
        return self.name
    def getArrival(self):
        return self.arrival
    def getDeparture(self):
        return self.departure
    def getPassengers(self):
        return self.passengers
    
    def getAllData(self):
        return[self.name,self.departure,self.arrival,self.destination,self.gate ,self.passengers]



if __name__ == '__main__':
    datetime_str = '19/6/18 13:55:26'
    datetime_str2 = '19/6/18 15:00:00'
    datetime_object = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S')
    datetime_object2 = datetime.strptime(datetime_str2, '%d/%m/%y %H:%M:%S')
    print(datetime_str)
    print(diff := datetime_object2 - datetime_object)
    print(datetime_object + diff)