// Zak's javascript selection sort function:

// Create an array of random numbers between 1 and 10
function createRandomArray(itemNum) {
  array = [];
  for (var i = 0; i < itemNum; i++) {
    array.push(Math.floor(Math.random() * 10) + 1);
  }
  return array;
}

// Selection sort function
function selectionSort(array) {
  console.log("Starting array:");
  console.log(array);
  console.log("Running selection sort...");

  // Set up currentSortIndex. When currentSortIndex
  // reaches the second to last position in the list, 
  // we are done.
  for (var currentSortIndex = 0; currentSortIndex < array.length - 1; currentSortIndex++) {

    // Start minIndex at the currentSortIndex. Loop through
    // the array. Record the position of the smallest number
    // in the array to minIndex.
    var minIndex = currentSortIndex;
    for (var i = currentSortIndex; i < array.length; i++) {
      // Find the lowest number in the array and swap
      // it with the currentSortIndex
      if (array[i] < array[minIndex]) {
        minIndex = i;
      }

    }
    // Swap the array values at currentSortIndex and minIndex
    var temp = array[currentSortIndex];
    array[currentSortIndex] = array[minIndex];
    array[minIndex] = temp;

    // uncomment me to see the selection swap at work:
    // console.log("swapped position " + currentSortIndex + " with " + minIndex)
    // console.log(array);
  }
  return array;
}

// Run the function(s) and print the sorted array
console.log(selectionSort(createRandomArray(10)));
