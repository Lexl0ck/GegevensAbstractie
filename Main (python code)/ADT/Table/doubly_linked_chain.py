class doubly_linked_chain:
    ''' A chain of containers linked together by pointers without order. '''

        
    class node:
        ''' A container with two pointers one pointing to the previous one pointing to the next element.
            A new node is created by giving it an an item and the two links.
            Example: node(previous Node, item, next node)
            The searchkey for a node is its item if its a single value or its first object if it's a list.'''
        def __init__(self,prevNode,item,nextNode, searchKey = 0):
            self.next = nextNode
            self.prev = prevNode
            self.item = item
            if searchKey == 0:
                self.searchKey = item
                if type(item) == type([]):
                    self.searchKey = item[0]
            else:
                self.searchKey = searchKey

                
    
    def __init__(self):
        dummy_head_node = self.node(None,None,None) #a dummy head Node to prevent the special case of inserting at the head.
        self.headPtr = dummy_head_node
        self.tailPtr = dummy_head_node
        self.length = 0

    def __reset_tailPtr(self):
        ''' Sets the tail pointer to the last Position again in case something is added or removed from the tail of the chain. '''
        def isLastNode(node):
            if node.next == None:
                return node
        self.tailPtr = self.traverse(isLastNode)
            

    def insert(self,item, searchkey=0):
        ''' Adds an item to the front of the chain after the dummy head node.'''
        dummyHeadNode = self.headPtr
        nextNode = dummyHeadNode.next
        tmpNode = self.node(dummyHeadNode,item,dummyHeadNode.next,searchkey)
        dummyHeadNode.next = tmpNode
        if nextNode != None:
            nextNode.prev = tmpNode
        self.length +=1
        self.__reset_tailPtr()


    def traverse(self,visit):
        ''' Traverses the chain from the head to the tail calling visit(current node) at each node.
            If visit is a fruitfull function the traversal will be stopped when another value than
            None is returned and the by visit returned value will be returned by traverse().
        '''
        tmpNode = self.headPtr
        tmpNode = tmpNode.next #skip the dummy head node
        while tmpNode != None:
            tmp = visit(tmpNode)
            if tmp != None:
                return tmp
            tmpNode = tmpNode.next

    def remove(self,searchKey):
        ''' Removes the first node with the given searchkey from the chain.
            The method returns True if it was successfull or False if not.
        '''
        tmp = self.getNode(searchKey)
        
        if tmp == None:
            return False
        prevNode = tmp.prev
        nextNode = tmp.next
        prevNode.next = nextNode
        if nextNode != None:
            nextNode.prev = prevNode
        self.length -=1
        self.__reset_tailPtr()
        return True


    def clear(self):
        ''' Removes all the nodes from the chain except for the dummy head node. '''
        dummyHeadNode = self.headPtr
        dummyHeadNode.next = None
        self.tailPtr = dummyHeadNode
        

    def getNode(self,searchKey):
        ''' Returns the first node found with the given searchkey.'''
        def compare(node):
            if node.searchKey == searchKey:
                return node
        return self.traverse(compare)

    def getItem(self, searchKey):
        ''' Returns the first item found with the given searchkey. '''
        node = self.getNode(searchKey)
        if node:
            return node.item
        else:
            return False

    def isEmpty(self):
        ''' Returns True if the chain is empty or false if not. '''
        if self.tailPtr is None:
            return True
        return False

    def getTraverse(self):
        ''' returns a list of all the items in the chain '''
        tmpList = []
        tmpNode = self.headPtr
        tmpNode = tmpNode.next #skip the dummy head node
        while tmpNode != None:
            tmpList.append(tmpNode.item)
            tmpNode = tmpNode.next
        return tmpList

