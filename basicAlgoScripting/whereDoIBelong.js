function getIndexToIns(arr, num) {
    // Find my place in this sorted array.
    if (arr.length == 0) {
        return 0;
    }
    let sorted = arr.sort((x, y) => x > y);
    for (let i = 0; i < sorted.length; i++) {
        if (sorted[i] > num || sorted[i] == num) {
            return i;
        } else if (Math.max(...sorted) < num) {
            return sorted.length;
        }
    }
}

console.log(getIndexToIns([40, 60], 50));
console.log(getIndexToIns([1, 2, 3, 4], 1.5));
console.log(getIndexToIns([20, 3, 5], 19));
console.log(getIndexToIns([10, 20, 30, 40, 50], 35));
console.log(getIndexToIns([10, 20, 30, 40, 50], 30));
console.log(getIndexToIns([40, 60], 50));
console.log(getIndexToIns([5, 3, 20, 3], 5));
console.log(getIndexToIns([2, 20, 10], 19));
console.log(getIndexToIns([2, 5, 10], 15));
console.log(getIndexToIns([], 1));