class Film:

    def __init__(self):
        self.ID = 0
        self.title = ""
        self.rating = 0.00
   
    def setID(self, ID):
        self.ID = ID

    def setTitle(self, title):
        self.title = title

    def setRating(self, rating):
        self.rating = rating

    def getID(self):
        return self.ID

    def getTitle(self):
        return self.title

    def getRating(self):
        return self.rating

    def __eq__(self, other):
        return self.rating == other.rating
 
    def __ne__(self, other):
        return not self.rating == other.rating

    def __lt__(self, other):
        return self.rating < other.rating

    def __le__(self, other):
        return self.rating <= other.rating

    def __gt__(self, other):
        return self.rating > other.rating
   
    def __ge__(self, other):
        return self.rating >= other.rating