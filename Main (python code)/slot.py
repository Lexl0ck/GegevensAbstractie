class Slot:

    def __init__(self):
        self.ID = 0
        self.time = "..:.."

    def setID(self, ID):
        self.ID = ID

    def setTime(self, time):
        self.time = time

    def getID(self):
        return self.ID

    def getTime(self):
        return self.time

    def __eq__(self, other):
        return self.ID == other
 
    def __ne__(self, other):
        return not self.ID == other

    def __lt__(self, other):
        return self.ID < other

    def __le__(self, other):
        return self.ID <= other

    def __gt__(self, other):
        return self.ID > other
   
    def __ge__(self, other):
        return self.ID >= other
