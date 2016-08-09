# Zak's doubleLinkedList practice.
# To-do:
#    search,
#    delete,


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

    def jumpPrev(self, int=1):
        node = self
        while int > 0:
            node = node.getPrev()
            int -= 1
        return node


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

    # Insert node will insert a node AFTER the specified position, starting
    # from 0. If there's no param supplied, set as new head (not implemented)
    def insertNode(self, data, position):  # position=self.size()):
        newNode = Node(data)
        node = self.head.jumpNext(position)
        # Checks to make sure we're not already in the last position.
        # If so, set the prev value, otherwise set the new node to tail.
        if node.getNext() is not None:
            newNode.next = node.getNext()
            node.getNext().prev = newNode
            newNode.prev = node
            node.next = newNode
        else:
            newNode.prev = node
            node.next = newNode
            self.tail = newNode

    def size(self):
        # Pass through nodes, incrementing numNodes until you reach the end
        # Currently it doesn't return 0 on an empty list lol.
        # maybe `if self.head is not None: ... else: return 0`
        if self.head is not None:
            node = self.head
            numNodes = 1
        else:
            return 0
        while node.getNext() is not None:
            numNodes += 1
            node = node.getNext()
        return numNodes

    # Gotta think about this one... You should be able to search through the
    # data in each node, but would you return the node info for each that
    # matches?
    def search(self):
        pass

    def delete(self, position):
        node = self.head.jumpNext(position)
        # If there's no next or previous, we're at head or tail and must
        # reset those attributes
        if node.getPrev() is not None:
            node.getPrev().next = node.getNext()
        else:
            self.head = node.getNext()
        if node.getNext() is not None:
            node.getNext().prev = node.getPrev()
        else:
            self.tail = node.getPrev()
        # node.garbageDay()

    def printAll(self):
        node = self.head
        i = 0
        while i < self.size():
            print "Node {0}: {1}".format(i, node.data)
            node = node.getNext()
            i += 1

# Some nodes to play around with:
list = LinkedList()
list.addNode("first")
list.addNode("second")
list.addNode("third")

list.insertNode("second.2", 1)
# list.insertNode("without a position, this should default to the beginning")

list.printAll()

print "About to delete position 3.."
list.delete(3)

list.printAll()
