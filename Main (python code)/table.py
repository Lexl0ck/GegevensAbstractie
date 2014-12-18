from binarytree import *
from doubly_linked_chain import *

from hashmap import *
from redblack_tree import *
from tree_234 import *
from TwoThreeTree import * 


class Table:

    def __init__(self):
        self.implementation = "binaryTree"
        self.pointer = None
        
    def setImplementation(self, implementation):
        self.implementation = implementation

    def createTable(self):
        if self.implementation == "binaryTree":
            self.pointer = BinTree()
        elif self.implementation == "doublylinkedchain":
            self.pointer = Doubly_linked_chain()
        elif self.implementation == "hashmap":
            self.pointer = Hashmap()
        elif self.implementation == "redBlackTree":
            self.pointer = Redblacktree()
        elif self.implementation == "234Tree":
            self.pointer = Tree234()
        elif self.implementation == "23Tree":
            self.pointer = TwoThreeTree()

    def destroyTable(self):
        if (self.implementation == "binaryTree" or
           self.implementation == "doublylinkedchain"):
            self.pointer.clear()
        elif self.implementation == "hashmap":
            self.pointer.destroy()
        elif (self.implementation == "redBlackTree" or
              self.implementation == "234Tree" or
              self.implementation == "23Tree"):
            self.pointer.destroyTree()

    def tableIsEmpty(self):
        return self.pointer.isEmpty()  

    def tableLength(self):
        if self.implementation == "binaryTree":
            return len(self.pointer.inorder())
        elif self.implementation == "doublylinkedchain":
            return self.pointer.getLength()
        elif self.implementation == "hashmap":
            return self.pointer.getLength()
        elif self.implementation == "redBlackTree":
            return self.pointer.getLength()
        elif self.implementation == "234Tree":
            return self.pointer.getLength()
        elif self.implementation == "23Tree":
            return self.pointer.treeLength()

    def tableInsert(self, newItem):
        if (self.implementation == "doublylinkedchain" or
            self.implementation == "hashmap"):
            return self.pointer.insert(None, newItem)
        return self.pointer.insert(newItem)

    def tableDelete(self, searchKey):
        if self.implementation == "binaryTree":
            return self.pointer.remove(searchKey)
        elif self.implementation == "doublylinkedchain":
            return self.pointer.remove(searchKey)
        elif self.implementation == "hashmap":
            return self.pointer.remove(searchKey)
        elif self.implementation == "redBlackTree":
            return self.pointer.delete(searchKey)
        elif self.implementation == "234Tree":
            return self.pointer.delete(searchKey)
        elif self.implementation == "23Tree":
            return self.pointer.deleteItem(searchKey)

    def tableRetrieve(self, searchKey):
        if self.implementation == "binaryTree":
            return self.pointer.getData(searchKey)
        elif self.implementation == "doublylinkedchain":
            return self.pointer.getItem(searchKey)
        elif self.implementation == "hashmap":
            return self.pointer.getItem(searchKey)
        elif self.implementation == "redBlackTree":
            return self.pointer.search(searchKey)
        elif self.implementation == "234Tree":
            self.pointer.retrieve(searchKey)
        elif self.implementation == "23Tree":
            self.pointer.retrieveItem(searchKey)

    def traverseTable(self):
        if self.implementation == "binaryTree":
            return self.pointer.inorder()
        elif self.implementation == "doublylinkedchain":
            return self.pointer.getTraverse()
        elif self.implementation == "hashmap":
            return self.pointer.traverse()
        elif self.implementation == "redBlackTree":
            return self.pointer.inOrderTraversal()
        elif self.implementation == "234Tree":
            return self.pointer.traverse()
        elif self.implementation == "23Tree":
            return self.pointer.traverse()


