import tkinter as tk
from tkinter import ttk
import Add_to_database_AND_SELECT as db
import Flights
import AirportControl
import Information
from datetime import datetime
LARGE_FONT= ("Verdana", 12)



loty = Flights.Flights()
AirportControl = AirportControl.AirportControl(loty)
Information = Information.InformationSystem(loty)

loty.AddFlightsFromDatabase()
#print(Information.getFlights())


class main(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('1000x800')
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ControlSystem, InformationSystem,AddNewFlight,
                  ShowFlights, AddNewPassenger,DeletePassenger,DeleteFlight,
                  FlightInfo,DelayControl):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Wybór systemu", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="System kontroli lotniska",
                            command=lambda: controller.show_frame(ControlSystem))
        button.pack()

        button2 = tk.Button(self, text="System informacyjny",
                            command=lambda: controller.show_frame(InformationSystem))
        button2.pack()










class ControlSystem(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="System kontroli lotniska", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Powrót do wyboru systemu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Dodaj lot",
                            command=lambda: controller.show_frame(AddNewFlight))
        button2.pack()
        
        button3 = tk.Button(self, text="Dodaj pasażera",
                            command=lambda: controller.show_frame(AddNewPassenger))
        button3.pack()
        button4 = tk.Button(self, text="Usuń pasażera",
                            command=lambda: controller.show_frame(DeletePassenger))
        button4.pack()
        
        button5 = tk.Button(self, text="Usuń Lot",
                            command=lambda: controller.show_frame(DeleteFlight))
        button5.pack()
        
        button6 = tk.Button(self, text="Kontrola opóźnień",
                            command=lambda: controller.show_frame(DelayControl))
        button6.pack()
        # button2 = tk.Button(self, text="Page Two",
        #                     command=lambda: controller.show_frame(InformationSystem))
        # button2.pack()


class InformationSystem(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="System Informacyjny", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Powrót do wyboru systemu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        button2 = tk.Button(self, text="Pokaż odloty",
                            command=lambda: controller.show_frame(ShowFlights))
        button2.pack()

        button3 = tk.Button(self, text="Pokaż informacje o locie",
                            command=lambda: controller.show_frame(FlightInfo))
        button3.pack()

        # button2 = tk.Button(self, text="Page One",
        #                     command=lambda: controller.show_frame(ControlSystem))
        # button2.pack()
#def DodajLot(Nazwa, Numer_rejerstracyjny, model_samolotu, odlot, przylot, bramka,destynacja):
class AddNewFlight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Dodaj Lot", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        
        labelName = tk.Label(self, text="Nazwa Lotu: ").place(x=0,y=100)
        self.entryName = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryName.place(x=100,y=100)
        
        labelReg = tk.Label(self, text="Numer Rejerstracyjny: ").place(x=0,y=120)
        self.entryReg = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryReg.place(x=100,y=120)
        
        labelPlane = tk.Label(self, text="Model Samolotu: ").place(x=0,y=140)
        self.entryPlane = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryPlane.place(x=100,y=140)
        
        labelDep = tk.Label(self, text="Odlot: ").place(x=0,y=160)
        self.entryDep = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryDep.place(x=100,y=160)
        
        labelAr = tk.Label(self, text="Przylot: ").place(x=0,y=180)
        self.entryAr = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryAr.place(x=100,y=180)
        
        labelGate = tk.Label(self, text="Bramka: ").place(x=0,y=200)
        self.entryGate = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryGate.place(x=100,y=200)
        
        labelDest = tk.Label(self, text="Destynacja: ").place(x=0,y=220)
        self.entryDest = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryDest.place(x=100,y=220)
        
        
        #command=self.getData()
        
        buttonAdd = tk.Button(self, text="Dodaj",
                            command=self.AddFlight).place(x = 340, y= 340)
        
        buttonExit = tk.Button(self, text="Powrót do systemu kontroli",
                            command=lambda: controller.show_frame(ControlSystem)).place(x = 20, y= 340)
        #button1.pack()
        
        #'%d/%m/%y %H:%M:%S' np. ('19/6/18 13:55:26')
    def AddFlight(self):
        #    def addFlight(self, Nazwa, Numer_rejerstracyjny, model_samolotu, odlot, przylot, bramka, destynacja):
        #print('klik')
        
        AirportControl.addFlight(
            Nazwa = str(self.entryName.get()),
            Numer_rejerstracyjny= str(self.entryReg.get()),
            model_samolotu= str(self.entryPlane.get()),
            odlot= str(self.entryDep.get()),
            przylot= str(self.entryAr.get()),
            bramka= str(self.entryGate.get()),
            destynacja= str(self.entryDest.get())
        )
        print( str(self.entryName.get()),
            str(self.entryReg.get()),
            str(self.entryPlane.get()),
            str(self.entryDep.get()),
            str(self.entryAr.get()),
            str(self.entryGate.get()),
            str(self.entryDest.get())
        )
        loty.AddFlightsFromDatabase()
        
        
        
        
        
class AddNewPassenger(tk.Frame):
    def __init__(self, parent, controller):
        loty.AddFlightsFromDatabase()
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Dodaj pasażera", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        
        labelName = tk.Label(self, text="Numer biletu: ").place(x=0,y=100)
        self.entryTicket = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryTicket.place(x=100,y=100)
        
        labelReg = tk.Label(self, text="Imie: ").place(x=0,y=130)
        self.entryName = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryName.place(x=100,y=130)
        
        labelPlane = tk.Label(self, text="Nazwisko: ").place(x=0,y=160)
        self.entryLastName = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryLastName.place(x=100,y=160)
        
        labelDep = tk.Label(self, text="Nazwa lotu: ").place(x=0,y=190)
        
        self.entryFlightName =  ttk.Combobox(self,postcommand = self.UpdateCombobox )# values = loty.getNamesOfFlights())#tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryFlightName.place(x=100,y=190)
        
        
        
        labelAr = tk.Label(self, text="Typ bagażu: ").place(x=0,y=220)
        self.entryBag = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryBag.place(x=100,y=220)
        
        labelGate = tk.Label(self, text="Status odprawy: ").place(x=0,y=250)
        self.entryCheckIn = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryCheckIn.place(x=100,y=250)
        
        labelDest = tk.Label(self, text="Numer fotela: ").place(x=0,y=290)
        self.entrySeat = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entrySeat.place(x=100,y=290)
        
        
        #command=self.getData()
        
        buttonAdd = tk.Button(self, text="Dodaj",
                            command=self.AddPassenger).place(x = 340, y= 340)
        
        buttonExit = tk.Button(self, text="Powrót do systemu kontroli",
                            command=lambda: controller.show_frame(ControlSystem)).place(x = 20, y= 340)
        #button1.pack()
        
        #'%d/%m/%y %H:%M:%S' np. ('19/6/18 13:55:26')
    def AddPassenger(self):
        #    def addFlight(self, Nazwa, Numer_rejerstracyjny, model_samolotu, odlot, przylot, bramka, destynacja):
        #print('klik')
        loty.AddFlightsFromDatabase()
        AirportControl.addPassenger(
            self.entryTicket.get(),
            str(self.entryName.get()),
            str(self.entryLastName.get()),
            str(self.entryFlightName.get()),
            str(self.entryBag.get()),
            str(self.entryCheckIn.get()),
            self.entrySeat.get()
        )

        loty.AddFlightsFromDatabase()
    def UpdateCombobox(self):
        self.entries = loty.getNamesOfFlights()
        self.entryFlightName['values'] = self.entries
        
        
        
class ShowFlights(tk.Frame):

    def __init__(self, parent, controller):
        #self.geometry('400x800')
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Odloty", font=LARGE_FONT).grid(row = 0, columnspan = 5)
        #label.pack(pady=10,padx=10)
        cols = ('Nazwa','Destynacja','Odlot','Przylot','Bramka')
        self.tree = ttk.Treeview(self,columns = cols,show = 'headings')
        for col in cols:
            self.tree.heading(col,text = col)
        self.tree.grid(row = 1, column =0, columnspan = 5)
        #self.GetFlights









        button1 = tk.Button(self, text="Powrót do wyboru systemu",
                            command=lambda: controller.show_frame(InformationSystem)).grid(row = 4, column = 0)
        
        button2 = tk.Button(self, text="Pokaż odloty",
                            command=self.GetFlights).grid(row = 4, column = 4)
        #button1.pack()
        
    def GetFlights(self):
        
        self.tree.delete(*self.tree.get_children())
        loty.AddFlightsFromDatabase()
        #print(len(loty.getFlightsData()))
        flightsList = loty.getFlightsData()
        flightsList.sort(key=lambda e: e[1])
        for elem in flightsList:
            self.tree.insert("","end",values = (elem[0],elem[3],elem[1],elem[2],elem[4]))
            #print(elem)
            #print(elem)
        
        
        ...
        
        
        
class FlightInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Informacje o locie", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        self.text = tk.StringVar()
        self.text.set('Test')
        
        label2 = tk.Label(self, text=" ", font=LARGE_FONT)
        label2.pack(pady=10,padx=10)
        
        label3 = tk.Label(self, text="Wpisz numer lotu:", font=("Verdana", 10))
        label3.pack(pady=10,padx=10)
        
        self.entry = tk.Text(self,height = 1, width = 10)
        self.entry.pack()
        
        buttonGetInfo = tk.Button(self, text="Wyszukaj lot",
                            command= self.ShowInfo)
        buttonGetInfo.pack()
        self.label4 = tk.Label(self, textvariable = self.text, font=("Verdana", 10))
        self.label4.pack(pady=10,padx=10)
        
        buttonExit = tk.Button(self, text="Powrót do Systemu informacyjnego",
                            command=lambda: controller.show_frame(InformationSystem))
        buttonExit.pack()
    def ShowInfo(self):
        self.text.set(Information.showFlightInformation(str(self.entry.get("1.0",tk.END)).strip()))  # = Information.showFlightInformation(self.entry.get("1.0",tk.END))

        ...
    
    ...
        
        
class DeletePassenger(tk.Frame):
    def __init__(self, parent, controller):
        self.entries = loty.getPassengersFromAllFlights()
        loty.AddFlightsFromDatabase()
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Usuń pasażera", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        
        
        labelDep = tk.Label(self, text="Nazwa lotu: ")
        labelDep.pack()
        
        self.entryTicket =  ttk.Combobox(self, postcommand = self.UpdateCombobox    )        #values = self.entries)
        self.entryTicket.pack()
        
        
        
        buttonDel = tk.Button(self, text="Usuń",
                            command=self.Delete)
        buttonDel.pack()
        
        buttonExit = tk.Button(self, text="Powrót do Systemu kontroli",
                            command=lambda: controller.show_frame(ControlSystem))
        buttonExit.pack()
        
    def Delete(self):
        db.deletePassenger(self.entryTicket.get())
        
        loty.AddFlightsFromDatabase()
        self.entries = loty.getPassengersFromAllFlights()
        #loty.getPassengersFromAllFlights()
        
    def UpdateCombobox(self):
        self.entries = loty.getPassengersFromAllFlights()
        self.entryTicket['values'] = self.entries
        
        
        
        ...
        
        
        
        
class DeleteFlight(tk.Frame):
    def __init__(self, parent, controller):
        #self.entries = loty.getPassengersFromAllFlights()
        loty.AddFlightsFromDatabase()
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Usuń pasażera", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        
        
        labelDep = tk.Label(self, text="Nazwa lotu: ")
        labelDep.pack()
        
        self.entryFlight =  ttk.Combobox(self, postcommand = self.UpdateCombobox    )        #values = self.entries)
        self.entryFlight.pack()
        
        
        
        buttonDel = tk.Button(self, text="Usuń",
                            command=self.Delete)
        buttonDel.pack()
        
        buttonExit = tk.Button(self, text="Powrót do Systemu kontroli",
                            command=lambda: controller.show_frame(ControlSystem))
        buttonExit.pack()
        
    def Delete(self):
        #db.deletePassenger(self.entryTicket.get())
        
        loty.AddFlightsFromDatabase()
        self.entries = loty.getPassengersFromAllFlights()
        
        db.deleteFlight(self.entryFlight.get())
        loty.AddFlightsFromDatabase()
        #loty.getPassengersFromAllFlights()
        
    def UpdateCombobox(self):
        self.entries = loty.getNamesOfFlights()
        self.entryFlight['values'] = self.entries
        
        
class DelayControl(tk.Frame):
    def __init__(self, parent, controller):
        #self.entries = loty.getPassengersFromAllFlights()
        loty.AddFlightsFromDatabase()
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Kontrola opóźnień", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        

        self.text = tk.StringVar()
        self.text.set('Wprowadź Dane')
        
        
        
        labelFlightName = tk.Label(self, text="Nazwa opóźnionego lotu: ")
        labelFlightName.pack()
        self.entryFlight =  ttk.Combobox(self, postcommand = self.UpdateCombobox    )        #values = self.entries)
        self.entryFlight.pack()
        
        labelDelay = tk.Label(self, text="Wpisz opóźnienie (w minutach): ")
        labelDelay.pack()
        
        self.entryDelay = tk.Entry(self,bd = 5) #.place(x=100,y=100)
        self.entryDelay.pack()
        
        buttonDelay = tk.Button(self, text="Akceptuj",
                            command=self.Control)
        buttonDelay.pack()
        
        self.label4 = tk.Label(self, textvariable = self.text, font=("Verdana", 10))
        self.label4.pack(pady=10,padx=10)
        
        
        labelNULL = tk.Label(self, text="")
        labelNULL.pack()
        labelNULL = tk.Label(self, text="")
        labelNULL.pack()
        buttonExit = tk.Button(self, text="Powrót do Systemu kontroli",
                            command=lambda: controller.show_frame(ControlSystem))
        buttonExit.pack()
    
    def UpdateCombobox(self):
        self.entries = loty.getNamesOfFlights()
        self.entryFlight['values'] = self.entries
        
    def Control(self):
        Dep, tmp = AirportControl.DelayControl(str(self.entryFlight.get()).strip(),int(self.entryDelay.get()))
        
        self.text.set('Nowa data wylotu: ' + Dep)
        loty.AddFlightsFromDatabase()
        
        ...
        
print(loty.getNamesOfFlights())
app = main()
app.mainloop()
