import os
from movietheatre import * 

theatre = Movietheatre()

# defining function clear to clear the screen.
# call "clear" on linux, "cls" on windows.
if os.name == "nt":
    def clear():
        os.system("cls")
else:
    def clear():
        os.system("clear")
        

def create_reservation():
    ''' Asks for input and creates a reservation '''
    print("** making reservation ***********")
    userID = input("Please enter your user ID: ")
    showingID = input("Please enter a showing ID: ")
    amount = input("How many tickets would you like? ")
    if theatre.makeReservation(reservationID, userID, showingID, amount):
        print("reservation made. press any key to return")
    else:
        print("reservation failed. press any key to return")
    input("")

def create_user():
    ''' Asks for input and creates a user '''
    print("** creating user ***********")
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    email = input("Please enter your e-mail: ")
    if theatre.makeReservation(userID, firstname, lastname, email):
        print("Reservation made. press any key to return")
    else:
        print("Reservation failed. press any key to return")
    input("")

def create_film():
    ''' Asks for input and creates a film '''
    print("** adding a new film ***********")
    title = input("Please enter the title: ")
    rating = input("Please enter a rating: ")
    if theatre.addFilm(filmID, title, rating):
        print("Film Added. press any key to return")
    else:
        print("Couldn't add film. press any key to return")
    input("")

def create_showing():
    ''' Asks for input and creates a showing '''
    print("** adding a new showing ***********")
    screenID = input("Please enter the screenID: ")
    timeslot = input("Please choose the timeslot: ")
    date = input("Please enter the date: ")
    filmID = input("Please enter the filmID: ")
    if theatre.addShowing(screenID, timeslot, date, filmID):
        print("Showing added. press any key to return")
    else:
        print("Couldn't add showing. press any key to return")
    input("")

def checkin():
    ''' get a showing ID and check in viewers for that showing '''
    print("** checking in ********************")
    showingID = input("Please input the showing ID")
    answer = "y"
    print("Now checking in for showing with ID: ",showingID)
    while answer == "y":
        answer = input("type 'y' to check in a viewer, any other key to stop checking in")
        theatre.checkin(showingID)

def reservationmenu():
    ''' shows reservation menu, executes chozen input '''
    while True:
        clear()
        print("== RESERVATION MENU ==\n")
        print("Make your choice:\n")
        print(" 0. Return to main menu")
        print(" 1. Reserve for existing userID")
        print(" 2. Reserve for new user")
        choice = input("\n> ")
        if int(choice) == 0: return True
        elif int(choice) == 1:
            create_reservation()
        elif int(choice) == 2:
            create_user()
            create_reservation()

def filmsmenu():
    ''' shows films menu, executes chozen input '''
    while True:
        clear()
        print("== FILMS MENU ==\n")
        print("Make your choice:\n")
        print(" 0. Return to main menu")
        print(" 1. Add a film")
        print(" 2. List films")
        choice = input("\n> ")
        if int(choice) == 0: return True
        elif int(choice) == 1:
            create_film()
        elif int(choice) == 2:
            for film in theatre.listFilms():
                print(film)
            input("Press any key to continue")

def showingsmenu():
    ''' prints showing menu, executes chozen input '''
    while True:
        clear()
        print("== SHOWINGS MENU ==\n")
        print("Make your choice:\n")
        print(" 0. Return to main menu")
        print(" 1. Add a showing")
        print(" 2. List showings")
        print(" 3. check in viewers for a showing")
        choice = input("\n> ")
        if int(choice) == 0: return True
        elif int(choice) == 1:
            create_showing()
        elif int(choice) == 2:
            for showing in theatre.listShowings():
                print(showing)
            input("Press any key to continue")
        elif int(choice) == 3:
            checkin()


def mainmenu():
    ''' prints the main menu and calls submenus '''
    while True:
        clear()
        print("== MAIN MENU ==\n")
        print("Make your choice:\n")
        print(" 1. Make reservation")
        print(" 2. Manage showings")
        print(" 3. Manage films")
        print(" 4. Quit")
        choice = input("\n> ")
        if int(choice) == 1: 
            reservationmenu()
        elif int(choice) == 2: 
            showingsmenu()
        elif int(choice) == 3: 
            filmsmenu()
        elif int(choice) == 4:
            return 0
        


# Call our main menu to get the ball rolling
mainmenu()
