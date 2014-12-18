class Linknode:
    ''' Represents a node in a chain. '''
    def __init__(self, data, pointer=None):
        ''' Initialise the node. '''
        self.data = data
        self.pointer = pointer

    def getPointer(self):
        ''' Returns the pointer of the node. '''
        return self.pointer

    def setPointer(self, pointer):
        ''' Sets the pointer of the node. ''' 
        self.pointer = pointer

    def getData(self):
        ''' Returns the data of the node '''
        return self.data


class Queue:
    ''' Represents the ADT Queue '''

    def __init__(self, front=None):
        ''' Creates a queue '''
        self.front = front
        self.tail = front

    def __str__(self):
        ''' Returns the current items in the queue formatted as a list '''
        pointer = self.front
        returnstring = []
        while not pointer == None:
            returnstring.append(pointer.getData())
            pointer = pointer.getPointer()
        return str(returnstring)

    def isEmpty(self):
        ''' Returns whether the queue is empty. '''
        if self.front == None:
            return True
        return False

    def enqueue(self, item):
        ''' Adds an item to the queue. '''
        previoustail = self.tail 
        self.tail = Linknode(item)
        if self.isEmpty():
            self.front = self.tail
        else:
            previoustail.setPointer(self.tail)
        return True

    def dequeue(self):
        ''' Removes and returns the front of the queue. '''
        if self.isEmpty():
            return False
        front = self.front
        self.front = self.front.getPointer()
        if self.front == None:
            self.tail = None
        return front.getData()
   
    def getFront(self):
        ''' Returns the front of the queue '''
        if self.isEmpty():
            return False
        return self.front.getData()


