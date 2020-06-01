let haStr = "Hazzzzah";
let haRegex = /Haz{4,}/; // Change this line
let result = haRegex.test(haStr);

console.log(result);
console.log("Hazzah".match(haRegex))
console.log("Hazzzah".match(haRegex))