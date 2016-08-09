# Zak's doubleLinkedList practice.
# To-do:
#    search,
#    delete,
#    some sorting/insert at position


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

    def delete(self):
        pass

# Some nodes to play around with:
list = LinkedList()
list.addNode(18)
