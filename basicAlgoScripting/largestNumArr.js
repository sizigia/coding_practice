function largestOfFour(arr) {
    let largNums = [];
    for (let i = 0; i < arr.length; i++) {
        largNums.push(Math.max(...arr[i]));
    }
    return largNums;
}

console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));
console.log(largestOfFour([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]), "should return: ", [27, 5, 39, 1001])