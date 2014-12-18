from Handlers.showing import *
from Containers.screen import *
from Containers.film import *
from Containers.reservation import *

from ADT.Table.table import *
from ADT.queue import *
from datetime import time
from datetime import date

class Movietheatre:

    def __init__(self):
        # Queue for reservations
        self.reservationQueue = Queue()
        self.reservationQueue.createQueue()

        # Tables (Showing and Film)
        self.showing_table = Table()
        self.showing_table.setImplementation("DoubleLinkedChain")
        self.showing_table.createTable()

        self.film_table = Table()
        self.film_talbe.createTable()

        self.reservation_table = Table()
        self.reservation_table.createTable()
       
 
        # Populate datastructures
        self.screens = []
        self.slots = []
        self.dates = []

        s1 = self.addScreen(0, 200)
        s2 = self.addScreen(1, 150)
 
        sl1 = self.init_slot(0, datetime.time(14,30))  # 14:30
        sl2 = self.init_slot(1, datetime.time(17))  # 17:00
        sl3 = self.init_slot(2, datetime.time(20))  # 20:00
        sl4 = self.init_slot(3, datetime.time(21,30)) # 22:30   


        f1 = self.addFilm(0, "Bloody Mary", 6.75)
        f2 = self.addFilm(1, "Star Wars", 2.25)
        f3 = self.addFilm(2, "Clockwork Orange", 8.56)
        f3 = self.addFilm(3, "Shining", 4.52)
        f4 = self.addFilm(4, "V for vendetta", 9.85)

        showing1 = self.addShowing(0, self.screens[0].getID(), 
        self.slots[2], datetime.date(2014,12,25), f2.getID(), self.screens[0].getSeats())

        showing2 = self.addShowing(1, self.screens[1].getID(), 
        self.slots[3], datetime.date(2014,12,25), f1.getID(), self.screens[1].getSeats())

        showing3 = self.addShowing(2, self.screens[1].getID(), 
        self.slots[3],datetime.date(2014,12,26), f4.getID(), self.screens[1].getSeats())

    def addScreen(self, screennumber, seats):
        screen = Screen()
        screen.setScreenNumber(screennumber)
        screen.setSeats(seats)
        self.screens.append(screen)

    def addSlot(self, slotID, time):
        slot = Slot()
        slot.setID(slotID)
        slot.setTime(time)
        self.slots.append(slot)
          
    def addFilm(self, filmdID, title, rating):
        film = Film()
        film.setID(filmID)
        film.setTitle(title)
        film.setRating(rating)
        self.film_table.tableInsert(film)

    def addShowing(self, showID, screenID, timeSlot, date, filmID, freeseats):
        showing = Showing()
        showing.setID(showID)
        showing.setScreenID(screenID)
        showing.setTimeSlot(filmdID)
        showing.setDate(date)
        showing.setFilmID(filmdID)
        showing.setFreeSeats(freeseats)
        self.showing_table.tableInsert(showing)

    def makeReservation(self, reservationID, userID, showingID, amount):
        reservation = Reservation()
        reservation.setId(reservationID)
        reservation.setTimestamp(datetime.datetime.now())
        reservation.setShowingID(showingID)
        reservation.setAmount(amount)
        self.reservationQueue.enqueue(reservation)
        pr_res = self.reservationQueue.dequeue(reservation)
        showing = self.getShowing(showingID)
        self.reservation_table.tableInsert(reservation)
        if showing.getFreeSeats() - amount > 0:
            return showing.reserve(amount)
        return False

    def listShowings(self):
       return self.showing_table.traverseTable()
   
    def getShowing(self, showingID):
       return showing_table.tableRetrieve(showingID)

    def removeShowing(self, showingID):
       return showing_table.tableDelete(showingID)

    def listFilms(self):
       return film_table.traverseTable()

    def getFilm(self, filmID):
       return film_table.tableRetrieve(filmID)

    def removeFilm(self, filmID):
       return film_table.tableDelete(filmID)
