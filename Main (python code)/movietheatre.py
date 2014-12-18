from showing import *
from screen import *
from film import *
from reservation import *
from slot import *
from user import *

from table import *
from queue import *
from datetime import *

class Movietheatre:

    def __init__(self):
        # Queue for reservations
        self.reservationQueue = Queue()
        self.reservationQueue.createQueue()

        # Tables (Showing and Film)
        self.showing_table = Table()
        self.showing_table.setImplementation("doublylinkedchain")
        self.showing_table.createTable()

        self.film_table = Table()
        self.film_table.createTable()

        self.reservation_table = Table()
        self.reservation_table.createTable()
       
 
        # Populate datastructures
        self.screens = []
        self.slots = []
        self.dates = []
        self.users = []

        s1 = self.addScreen(0, 200)
        s2 = self.addScreen(1, 150)
 
        sl1 = self.addSlot(0, time(14,30))  # 14:30
        sl2 = self.addSlot(1, time(17))  # 17:00
        sl3 = self.addSlot(2, time(20))  # 20:00
        sl4 = self.addSlot(3, time(21,30)) # 22:30   


        f1 = self.addFilm(0, "Bloody Mary", 6.75)
        f2 = self.addFilm(1, "Star Wars", 2.25)
        f3 = self.addFilm(2, "Clockwork Orange", 8.56)
        f3 = self.addFilm(3, "Shining", 4.52)
        f4 = self.addFilm(4, "V for vendetta", 9.85)

        self.addShowing(0, self.screens[0].getScreenNumber(), 
        self.slots[2], date(2014,12,25), f2.getID(), self.screens[0].getSeats())

        self.addShowing(1, self.screens[1].getScreenNumber(), 
        self.slots[3], date(2014,12,25), f1.getID(), self.screens[1].getSeats())

        self.addShowing(2, self.screens[1].getScreenNumber(), 
        self.slots[3], date(2014,12,26), f4.getID(), self.screens[1].getSeats())

    def addScreen(self, screennumber, seats):
        screen = Screen()
        screen.setScreenNumber(screennumber)
        screen.setSeats(seats)
        self.screens.append(screen)
        return screen

    def addSlot(self, slotID, time):
        slot = Slot()
        slot.setID(slotID)
        slot.setTime(time)
        self.slots.append(slot)
        return slot

    def addUser(self, userID, firstname, lastname, email):
        user = User()
        user.setID(userID)
        user.setFirstName(firstname)
        user.setLastName(lastname)
        user.setEmail(email)
        self.users.append(user)
          
    def addFilm(self, filmID, title, rating):
        film = Film()
        film.setID(filmID)
        film.setTitle(title)
        film.setRating(rating)
        self.film_table.tableInsert(film)
        return film

    def addShowing(self, showID, screenID, timeSlot, date, filmID, freeseats):
        showing = Showing()
        showing.setID(showID)
        showing.setScreenID(screenID)
        showing.setTimeSlot(timeSlot)
        showing.setDate(date)
        showing.setFilmID(filmID)
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

    def listUsers(self):
       return self.users

    def listReservations(self):
       return self.film_table.traverseTable()
