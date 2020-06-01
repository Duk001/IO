import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='lotnisko',
                                         user='root',
                                         password='')
    mySql_insert_query = """INSERT INTO pasazer (Numer_biletu , Imie, Nazwisko, Nazwa_lotu) 
                           VALUES 
                           ('10', 'Maciej', 'Doktor', 'Jak najdalej stad') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Rekord zostal prawidlowo dodany")
    cursor.close()

except mysql.connector.Error as error:
    print("Nastapil problem przy dodawaniu rekordu {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("Polaczenie z MySQL zostalo zakonczone")