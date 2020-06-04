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
    return print(data)

def wysz_rekordu(info, tab):
    return(f"SELECT * FROM {tab} WHERE Imie LIKE '%{info}%'")
def wys_wszystko(info, tab) :
    return(f"SELECT {info} FROM {tab}")

imie_pasazera = wyswietl(wysz_rekordu('Maciej','pasazer'))
wszystkie_informacje = wyswietl(wys_wszystko('Imie','pasazer'))
sql = '''INSERT INTO pasazer (Numer_biletu , Imie, Nazwisko, Nazwa_lotu) VALUES ('11', 'Maciej', 'Doktor', 'Jak najdalej stad')'''
dodawanie = dodaj(sql)
