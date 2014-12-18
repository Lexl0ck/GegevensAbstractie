class Screen:

    def __init__(self):
        self.screenNumber = 0
        self.seats = 0    

    def setScreenNumber(self, screenNumber):
        self.screenNumber = screenNumber

    def setSeats(self, seats):
        self.seats = seats

    def getScreenNumber(self):
        return self.screenNumber

    def getSeats(self):
        return self.seats

    def __eq__(self, other):
        return self.screenNumber == other.screenNumber
 
    def __ne__(self, other):
        return not self.screenNumber == other.screenNumber

    def __lt__(self, other):
        return self.screenNumber < other.screenNumber

    def __le__(self, other):
        return self.screenNumber <= other.screenNumber

    def __gt__(self, other):
        return self.screenNumber > other.screenNumber
   
    def __ge__(self, other):
        return self.screenNumber >= other.screenNumber
 