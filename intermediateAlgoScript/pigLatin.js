function translatePigLatin(str) {
    if ('aeiou'.includes(str[0])) {
        return str + 'way';
    } else {
        let ind = str.split('').findIndex(x => 'aeiou'.includes(x));
        if (ind == -1) {
            return str + 'ay';
        } else { return str.slice(ind) + str.slice(0, ind) + 'ay'; }
    }
}

console.log(translatePigLatin("consonant"));
console.log(translatePigLatin("california"));
console.log(translatePigLatin("paragraphs"));
console.log(translatePigLatin("glove"));
console.log(translatePigLatin("algorithm"));
console.log(translatePigLatin("eight"));