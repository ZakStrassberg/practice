# Zak's python bubble sort function:
import random # need this for random.randint()

# Create an array of random numbers between 1 and 10
def createRandomList(itemNum):
    # pretty cool list creation code. I never reference
    # i, so maybe it can be simplified ever further...
    list = [random.randint(1,10) for i in range(itemNum)]
    return list

# Bubble sort function.
def bubbleSort(list):
    print "Starting array:"
    print list
    print "Running bubble sort..."

    # Sorted is false if any positions were found to
    # be out of order per iteration. This means that
    # the array will be sorted until it iterates
    # through once without finding anything to sort.
    sorted = False
    while sorted == False:
        sorted = True

        # start the loop at one to avoid out of range
        # or undefined errors. Compare the current
        # index to the one before it. Swap them if
        # they are out of order. Also set sorted to
        # false so the while statement will fire again.
        for i in range(1, len(list)):
            if list[i] < list[i - 1]:
                sorted = False

                # Use a tuple to swap
                (list[i], list[i - 1]) = (list[i - 1], list[i])

                # uncomment me to see the swap in action:
                # print list

        # uncomment me to show # of iterations
        # print "Full pass through array"

    return list

# Run the function(s) and print the sorted array
print bubbleSort(createRandomList(10))
