function frankenSplice(arr1, arr2, n) {
    // It's alive. It's alive!
    let newArr = [...arr2];
    newArr.splice(n, 0, ...arr1);
    return newArr;
}

console.log(frankenSplice([1, 2, 3], [4, 5], 1));
console.log(frankenSplice([1, 2], ["a", "b"], 1));
console.log(
    frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2));