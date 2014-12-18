class User:

    def __init__(self):
        self.ID = 0
        self.firstname = "None"
        self.lastname = "None"
        self.email = "None"

    def setID(self, ID):
        self.ID = ID

    def setFirstName(self, firstname):
        self.firstname = firstname

    def setLastName(self, lastname):
        self.lastname = lastname
 
    def setEmail(self, email):
        self.email = email
 
    def getID(self):
        return self.ID

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getEmail(self):
        return self.email