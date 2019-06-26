let sampleWord = "bana12";
let pwRegex = /(?=\w{5,})(?=\D+\d{2})/; // Change this line
let result = pwRegex.test(sampleWord);

console.log(result);
console.log(pwRegex.test("astronaut"))
console.log(pwRegex.test("airplanes"))
console.log(pwRegex.test("banan1"))
console.log(pwRegex.test("bana12"))
console.log(pwRegex.test("abc123"))
console.log(pwRegex.test("123"))