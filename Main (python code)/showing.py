from stack import *
from ticket import *

class Showing:

    def __init__(self):
        self.ID = 0
        self.screenID = 0
        self.timeSlot = None
        self.date = None
        self.filmID = 0
        self.freeseats = 0
        self.tickets = Stack()
        self.tickets.createStack()

    def setID(self, ID):
        self.ID = ID

    def setScreenID(self, screenID):
        self.screenID = screenID

    def setTimeSlot(self, timeSlot):
        self.timeSlot = timeSlot

    def setDate(self, date):
        self.date = date

    def setFilmID(self, filmID):
        self.filmID = filmID

    def setFreeSeats(self, seats):
        self.freeseats = seats

    def getID(self):
        return self.ID

    def getScreenID(self):
        return self.screenID

    def getTimeSlot(self):
        return self.timeSlot

    def getDate(self):
        return self.date

    def getFilmID(self):
        return self.filmID

    def getFreeSeats(self):
        return self.freeseats

    def reserve(self, ticket_am):
        if not self.date == None and not self.time == None:
            dt = datetime.datetime.combine(datetime.date(self.date, timeSlot.getTime)
            if datetime.datetime.now() < dt:
                for i in range(ticket_am):
                    ticket = Ticket()
                    if not self.tickets.push(ticket):
                       return False
                    self.freaseats -= 1
                return True   
        return False 
       
    def checkIn(self):
        if not self.date == None and not self.time == None:
            dt = datetime.datetime.combine(datetime.date(self.date, timeSlot.getTime)
            if dt < datetime.datetime.now() 
                if self.tickets.pop():
                    return True
        return False
        

    def __str__(self):
        return ("The variables of Showing: \n ID: "+str(self.getID())+"\n ScreenID: "+str(self.getScreenID())+ "\n TimeSlot: "+str(self.getTimeSlot())+ "\n Date: "+str(self.getDate())+
                "\n FilmID: "+str(self.getFilmID())+ "\n FreeSeats: "+str(self.getFreeSeats()))


 