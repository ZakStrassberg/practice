# Zak's javascript bubble sort function:
import random


# Create an array of random numbers between 1 and 10
def createRandomArray(itemNum):
    # pretty cool list creation code.
    list = [random.randint(1, 10) for i in range(itemNum)]
    return list


# Selection sort function.
def selectionSort(list):
    print "Starting list:"
    print list
    print "Running selection sort..."

    # Set up currentSortIndex. When currentSortIndex reaches
    # the second to last position in the list, we are done.
    for currentSortIndex in range(len(list) - 1):

        # Start minIndex at the currentSortIndex. Loop
        # through the list, record the position of the
        # smallest number in the list to minIndex.
        minIndex = currentSortIndex
        for i in range(currentSortIndex, len(list)):
            if list[i] < list[minIndex]:
                minIndex = i

        # Swap currentSortIndex and minIndex
        (list[currentSortIndex], list[minIndex]) \
            = (list[minIndex], list[currentSortIndex])

        # Uncomment to see the swapped positions
        # print "Swapped position {} and {}".format(currentSortIndex, minIndex)
        # print list
        return list

# Run the function(s) and print the sorted array
print selectionSort(createRandomArray(10))
