function chunkArrayInGroups(arr, size) {
    // Break it up.
    let chunks = [];
    for (let i = 0; i < arr.length; i + size) {
        chunks.push([...arr.splice(i, size)]);
    }
    return chunks;
}

console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3));