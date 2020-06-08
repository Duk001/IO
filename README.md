<h1> Instrukcja uruchamiania prototypu: </h1>  
1. Proszę pobrać aplikację obsługująca serwer lokalny (np.XAMPP)<br />
2. Po przejściu przez wszystkie kroki instalator,  uruchomić aplikację<br /> 
3. Kliknąć Start na Apache oraz MySQL <br /> 
4. Uruchomić przeglądarkę i wpisać adres: http://localhost/phpmyadmin/ <br /> 
5. Utworzyć nową, pustą bazę danych o nazwie: lotnisko  <br />
6. Potem należy kliknąć Import i wybrać plik załączony w paczce o nazwie: lotnisko.sql  <br />
7. Przed uruchomieniem prototypu należy zaimportować moduł mysql.connector(pip install mysql.connector) <br /> 
8. Następnie po poprawnym zaimportowaniu bazy danych,oraz pobraniu modułów z repozytorium, uruchomić plik: GUI.py  <br />



***Uwaga: daty odlotów i przylotów należy podawać w następującym formacie: %dd/%mm/%yy %H:%M:%S np. (19/6/18 13:55:26)***
