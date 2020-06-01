const removeNull = (arr) => arr.filter(x => x !== null);

console.log(removeNull(['a', null, 'b', null]), ['a', 'b'])
console.log(removeNull([null, null, null, null, null]), [])
console.log(removeNull([7, 8, null, 9]), [7, 8, 9])
console.log(removeNull([7, null, 8, null, 9]), [7, 8, 9])