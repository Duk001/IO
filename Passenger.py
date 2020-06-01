class Passenger():
    def __init__(self,name, flightName, checkedBaggage, checkInStatus,ticket):
        '''
        ## Args: \n
            name: nazwa -> string 
            flightName: nazwa lotu -> string
            checkedBaggage: czy pasażer ma bagaż nadawany -> bool
            CheckInStatus: status odprawy -> string
            ticket: numer biletu -> string
            


        '''
        self.name = name
        self.flightName = flightName
        self.checkedBaggage = checkedBaggage
        self.checkInStatus = checkInStatus
        self.ticket = ticket

    def updateData(self, name, flightName, checkedBaggage,checkInStatus, ticket):

        '''
      ##  Args: \n
            name: nazwa -> string 
            flightName: nazwa lotu -> string
            checkedBaggage: czy pasażer ma bagaż nadawany -> bool
            CheckInStatus: status odprawy -> string
            ticket: numer biletu -> string
            
      ##  Returns:\n
            None

        '''
        
        self.name = name
        self.flightName = flightName
        self.checkedBaggage = checkedBaggage
        self.checkInStatus = checkInStatus
        self.ticket = ticket
    def getName(self):
        return self.name
    def getFlightName(self):
        return self.flightName
    def getCheckedBaggage(self):
        return self.checkedBaggage
    def getCheckInStatus(self):
        return self.checkInStatus
    def getTickets(self):
        return self.ticket
    def getAllData(self):
        return self.getName(), self.getFlightName(),self.getCheckedBaggage(),self.getCheckInStatus(),self.getTickets()