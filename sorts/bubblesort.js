// Zak's javascript bubble sort:

// Create an array of random numbers between 1 and 10
function createRandomArray(itemNum) {
    array = [];
    for (var i = 0; i < itemNum; i++) {
        array.push(Math.floor(Math.random() * 10) + 1);
    }
    return array;
}

// Bubble sort function.
function bubbleSort(array) {
    console.log("Starting array:");
    console.log(array);
    console.log("Running bubble sort...");

    // Sorted is false if any positions were found to
    // be out of order per iteration. This means that
    // the array will be sorted until it iterates
    // through once without finding anything to sort.
    var sorted = false;
    while (sorted === false) {
        sorted = true;

        // start the loop at one to avoid out of range
        // or undefined errors. Compare the current
        // index to the one before it. Swap them if
        // they are out of order. Also set sorted to
        // false so the while statement will fire again.
        for (var i = 1; i < array.length; i++) {
            if (array[i] < array[i - 1]) {
                sorted = false;
                var temp = array[i];
                array[i] = array[i - 1];
                array[i - 1] = temp
            }

            // uncomment me to see the swap in action:
            //console.log(array);
        }
        // uncomment me to show # of iterations
        //console.log("Full pass through array");
    }
    return array;
}

// Run the function(s) and print the sorted array
console.log(bubbleSort(createRandomArray(10)));
