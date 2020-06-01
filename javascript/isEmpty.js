const isEmpty = (obj) => Object.keys(obj).length < 1;

console.log(isEmpty({}), true)
console.log(isEmpty({ a: 1 }), false)
console.log(isEmpty({ z: 2, w: 4, y: 5 }), false)