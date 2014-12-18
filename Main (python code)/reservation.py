class Reservation:

    def __init__(self):
        self.ID = 0
        self.userID = 0
        self.timestamp = ""
        self.showingID = 0
        self.amount = 0
 
    def setID(self, ID):
        self.ID = ID

    def setUserID(self, userID):
        self.userID = userID

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def setShowingID(self, showingID):
        self.showingID = showingID

    def setAmount(self, amount):
        self.amount = amount

    def getID(self, ID):
        return self.ID

    def getUserID(self, userID):
        return self.userID

    def getTimestamp(self, timestamp):
        return self.timestamp

    def getShowingID(self, showingID):
        return self.showingID

    def getAmount(self, amount):
        return self.amount

    def __eq__(self, other):
        return self.ID == other.ID
 
    def __ne__(self, other):
        return not self.ID == other.ID

    def __lt__(self, other):
        return self.ID < other.ID

    def __le__(self, other):
        return self.ID <= other.ID

    def __gt__(self, other):
        return self.ID > other.ID
   
    def __ge__(self, other):
        return self.ID >= other.ID
 
    