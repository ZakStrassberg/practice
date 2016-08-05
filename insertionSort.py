# Zak's javascript bubble sort function:
import random


# Create an array of random numbers between 1 and 10
def createRandomArray(itemNum):
    # pretty cool list creation code.
    list = [random.randint(1, 10) for i in range(itemNum)]
    return list


# Insertion sort function.
def insertionSort(list):
    print "Starting list:"
    print list
    print "Running selection sort..."

    # Iterative over the array, starting from position 1
    for i in range(1, len(list)):

        # If the number at list[i] is less than the one
        # before it, save it as a variable.
        if (list[i-1] > list[i]):
                temp = list[i]

                # Loop backwards through the array, starting
                # from i. Move everything forward by 1 position
                # until the saved variable is greater than the
                # number at the [j-1] position. Replace the number
                # at [j] with what's in temp.
                j = i
                while (temp < list[j-1] and j > 0):
                        if (temp < list[j-1]):
                                list[j] = list[j-1]
                        j -= 1
                list[j] = temp

    return list

# Run the function(s) and print the sorted array
print insertionSort(createRandomArray(10))
