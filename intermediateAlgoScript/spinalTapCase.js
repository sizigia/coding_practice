function spinalCase(str) {
    // "It's such a fine line between stupid, and clever."
    // --David St. Hubbins
    return str.replace(/(?=[A-Z][a-z]*)|(?=[a-z]*)(\s|\W)/g, '-').toLowerCase();
}

console.log(spinalCase('This Is Spinal Tap'));
console.log(spinalCase("thisIsSpinalTap"));
console.log(spinalCase("The_Andy_Griffith_Show"));
console.log(spinalCase("Teletubbies say Eh-oh"));
console.log(spinalCase("AllThe-small Things"));