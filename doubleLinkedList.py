# Zak's doubleLinkedList practice.
# To-do:
#    search,
#    delete,
#    some sorting/insert at position
#
# Is there a way to implement getNext(4) to jump ahead 4 times?
# I am not so sure since I have to use return. Maybe with recursion.


# Nodes have a next and previous attribute, and contain a data attribute
# that can be accessed using .returnData()
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def returnData(self):
        return self.data

    def getNext(self):
        return self.next

    def jumpNext(self, int=1):
        node = self
        while int > 0:
            node = node.getNext()
            int -= 1
        return node

    def getPrev(self):
        return self.prev


# LinkedList class contains head and tail attributes
# Starts empty, new nodes can be added via function
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        # Create a new node with some data
        newNode = Node(data)
        # If the LinkedList is empty (no head), set the newNode as
        # both the head and the tail.
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        # Otherwise, set the current tail's next to newNode and the
        # newNode's prev to the previous tail. Then, set the LinkedList's
        # tail to the newNode.
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    # Insert node is NOT zero indexed!
    # this uses Node.next(int), which has NOT been tested yet!
    def insertNode(self, data, position):
        newNode = Node(data)
        node = self.head.jumpNext(position)
        node.getNext().prev = newNode
        node.next = newNode

    def size(self):
        # Pass through nodes, incrementing numNodes until you reach the end
        node = self.head
        numNodes = 1
        while node.getNext() is not None:
            numNodes += 1
            node = node.getNext()
            return numNodes

    def search(self):
        pass

    # Can I actually delete a node? This just removes reference of it from
    # the list. Is there a way to delete the pointer? Call garbage collection?
    def delete(self, position):
        node = self.head.jumpNext(position)
        node.getPrev.next = node.getNext()
        node.getNext.prev = node.getPrev()
        # node.garbageDay()

    def printAll(self):
        pass

# Some nodes to play around with:
list = LinkedList()
list.addNode(18)
