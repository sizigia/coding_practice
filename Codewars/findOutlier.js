function findOutlier(integers) {
    if (integers.filter(x => x % 2 == 0).length <= 1) {
        return integers.find(x => x % 2 == 0);
    } else {
        return integers.find(x => x % 2 != 0);
    }
}

console.log(findOutlier([0, 1, 2]), 1)
console.log(findOutlier([1, 2, 3]), 2)
console.log(findOutlier([2, 6, 8, 10, 3]), 3)
console.log(findOutlier([0, 0, 3, 0, 0]), 3)
console.log(findOutlier([1, 1, 0, 1, 1]), 0)