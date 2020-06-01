let username = "JackOfAllTrades";
let userCheck = /\D{2,}\d*$/; // Change this line
let result = userCheck.test(username);

console.log(result);

console.log(userCheck.test("JACK"))
console.log(userCheck.test("J"))
console.log(userCheck.test("Oceans11"))
console.log(userCheck.test("RegexGuru"), "RegexGuru".match(userCheck))
console.log(userCheck.test("007"))
console.log(userCheck.test("9"))