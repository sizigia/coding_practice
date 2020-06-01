function confirmEnding(str, target) {
    // "Never give up and good luck will find you."
    // -- Falcor
    let end = str.split('').splice(-target.length).join('');
    return end === target;
}

console.log(confirmEnding("Bastian", "n"));
console.log(confirmEnding("Congratulation", "on"));
console.log(confirmEnding("Connor", "n"));
console.log(
    confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification"), "should return false.");
console.log(confirmEnding("He has to give me a new name", "name"));