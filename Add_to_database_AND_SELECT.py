import mysql.connector

def dodaj(sql):
    connection = mysql.connector.connect(host='localhost', database='lotnisko', user='root', password='')
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    print(cursor.rowcount, 'Rekord zostal prawidlowo dodany')
    cursor.close()

def wyswietl(sql):
    connection = mysql.connector.connect(host='localhost', database='lotnisko', user='root', password='')
    cursor = connection.cursor()  
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return print(data)


def getFromDatabase(sql):
    connection = mysql.connector.connect(host='localhost', database='lotnisko', user='root', password='')
    cursor = connection.cursor()  
    cursor.execute(sql)
    data = cursor.fetchall()
    #print(data)
    return data

def wysz_rekordu(info, tab):
    return(f"SELECT * FROM {tab} WHERE Imie LIKE '%{info}%'")

def getSQLPasengersFromFlightFromDatabase(FlightName):
    return(f"SELECT * FROM pasazer WHERE Nazwa_lotu LIKE '%{FlightName}%'")
    
    ...
def wys_wszystko(info, tab) :
    return(f"SELECT {info} FROM {tab}")


#imie_pasazera = wyswietl(wysz_rekordu('Maciej','pasazer'))
# wszystkie_informacje = wyswietl(wys_wszystko('Imie','pasazer'))
# sql = '''INSERT INTO pasazer (Numer_biletu , Imie, Nazwisko, Nazwa_lotu) VALUES ('43', 'Maciej', 'Do', 'AF7777')'''
# dodawanie = dodaj(sql)




def DodajLot(Nazwa, Numer_rejerstracyjny, model_samolotu, odlot, przylot, bramka, destynacja):
    sql = f"INSERT INTO `lot` (`Nazwa_lotu`, `Numer_rejestracyjny`, `Model_samolotu`, `Godzina_odlotu`, `Godzina_przylotu`, `Bramka`, `Destynacja`) \
    VALUES ('{Nazwa}', '{Numer_rejerstracyjny}', '{model_samolotu}', '{odlot}', '{przylot}', '{bramka}', '{destynacja}')"
    dodaj(sql)
    
    #INSERT INTO `pasazer` (`Numer_biletu`, `Imie`, `Nazwisko`, `Nazwa_lotu`, `Typ_bagazu`, `Status_odprawy`, `Numer_fotela`) VALUES ('20', 'Adam', 'Kowalski', 'LF0021', ' checked baggage', 'Checked in', '46');
def DodajPasazera(Numer_biletu, Imie, Nazwisko, Nazwa_lotu, typ_bagazu, Status_odprawy, Numer_fotela):
    sql = f"INSERT INTO `pasazer` (`Numer_biletu`, `Imie`, `Nazwisko`, `Nazwa_lotu`, `Typ_bagazu`, `Status_odprawy`, `Numer_fotela`) \
    VALUES ('{Numer_biletu}', '{Imie}', '{Nazwisko}', '{Nazwa_lotu}', '{typ_bagazu}', '{Status_odprawy}', '{Numer_fotela}')"
    dodaj(sql)


def getFlightsFromDatabase():
    return getFromDatabase(wys_wszystko('*','lot'))

def getPassengersFromDatabase():
    return getFromDatabase(wys_wszystko('*','pasazer'))

def getPassengersListFromDatabase():
    flights = getFlightsFromDatabase()
    
    flightsList = []
    for flight in flights:
        flightsList.append(flight[0])
        
    passengers = []
    for elem in flightsList:
       passengers.append(getFromDatabase(getSQLPasengersFromFlightFromDatabase(elem)))
        
    return passengers 

def deletePassenger(ticketNumber):
    sql = f"DELETE FROM `pasazer` WHERE `pasazer`.`Numer_biletu` = {ticketNumber}"
    
    dodaj(sql)
    ...

def deleteFlight(flightName):
    sql_del_passengers = f"DELETE FROM `pasazer` WHERE `pasazer`.`Nazwa_lotu` = '{flightName}'"
    dodaj(sql_del_passengers)
    sql_del_flight = f"DELETE FROM `lot` WHERE `lot`.`Nazwa_lotu` = '{flightName}'"
    dodaj(sql_del_flight)
    
    
    ...

def getPassengersFromFlightFromDatabase(flightName):
    return getFromDatabase(getSQLPasengersFromFlightFromDatabase(flightName))
    
    


    
