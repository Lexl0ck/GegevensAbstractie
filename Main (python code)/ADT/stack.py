class Stack:
    '''
     Represents a Stack.
 
    Instance variables:
    self.stack = 0/[]

    Instance methods:
    createStack(self)
    destroyStack(self)
    isEmpty(self)
    push(self, newItem)
    pop(self)
    pop_r(self)
    getTop(self)
    '''


    def __init__(self):
        pass

    def createStack(self):
        '''Creates a new empty (list/)Stack.'''
        self.stack = []

    def destroyStack(self):
        '''Destroys the Stack.'''
        self.stack = 0

    def isEmpty(self):
        '''Checks if the Stack is Empty.

        return True/False
        Exceptions:
        NameError, AttributeError, TypeError
        //  return False
        '''

        try:
            return len(self.stack) == 0
        except (NameError, AttributeError, TypeError):
            return False

    def push(self, newItem):
        '''Pushes newItem on top of the Stack.

        Exceptions:
        NameError, AttributeError
        //  return False
        '''

        try:
            self.stack.append(newItem)
            return True
        except (NameError, AttributeError):
            return False

    def pop(self):
        '''Deletes the item on the top of the Stack.

        Exceptions:
        NameError, AttributeError, IndexError
        // returns False
        '''

        succes = True
        try:
            del self.stack[-1]
        except (NameError, AttributeError, IndexError):
            succes = False
        return succes

    def pop_r(self):
        '''Deletes the item on the top of the Stack and returns it.

        returns (stacktop, succes)
        Exceptions:
        NameError, AttributeError, IndexError
        // returns (-1, False)
        '''

        stackTop = -1
        succes = True
        try:
            stackTop = self.stack[-1];
            del stack[-1]
        except (NameError, AttributeError, IndexError):
            succes = False
        return (stackTop, succes)

    def getTop(self):
        '''Gets the top of the stack and returns it.

        returns (stacktop, succes)
        Exceptions:
        NameError, AttributeError, IndexError
        // returns (-1, False)
        '''

        stackTop = -1
        succes = True
        try:
            stackTop = self.stack[-1];
        except (NameError, IndexError):
            succes = False
        return (stackTop, succes)