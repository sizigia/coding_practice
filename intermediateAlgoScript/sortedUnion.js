function uniteUnique(...arr) {
    let newArr = [];
    let arrs = arguments.length;
    for (let i = 0; i < arrs; i++) {
        arguments[i].map(x => {
            if (!newArr.includes(x)) {
                // If you want to flatten the array, you can quickly fix it uncommenting the next line:
                // x.length == 1 ? newArr.concat(x) :
                newArr.push(x)
            }
        })
    }
    return newArr;
}

console.log(uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]))
console.log(uniteUnique([1, 3, 2], [1, [5]], [2, [4]]))
console.log(uniteUnique([1, 2, 3], [5, 2, 1]))
console.log(uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]))