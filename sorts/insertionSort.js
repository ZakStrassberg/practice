// Zak's javascript insertion sort function:

// Create an array of random numbers between 1 and 10
function createRandomArray(itemNum) {
    array = [];
    for (var i = 0; i < itemNum; i++) {
        array.push(Math.floor(Math.random() * 10) + 1);
    }
    return array;
}

// Insertion sort function
function insertionSort(array) {
    console.log("Starting array:");
    console.log(array);
    console.log("Running insertion sort...");

    // iterate over the array, starting from position one
    for (var i = 1; i < array.length; i++) {

        // if the number at [i] is less than the one before it,
        // save it as a variable.
        if (array[i - 1] > array[i]) {
            temp = array[i];

            // loop backwards through the array, starting from i.
            // move everything in the array forward 1 position
            // until the saved variable is greater than one the
            // number at the [j-1] position. Replace the number at
            // [j] with what's in temp.
            for (j = i; j > 0 && temp < array[j-1]; j--) {
                array[j] = array[j - 1];
            }
            array[j] = temp;
        }
    }
    return array;
}


// Run the function(s) and print the sorted array
console.log(insertionSort(createRandomArray(20)));
