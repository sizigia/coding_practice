function firstNonRepeatingLetter(s) {
    var chars = s.toLowerCase().split('');
    var check = chars.some(x => s.indexOf(x) == s.lastIndexOf(x));
    if (s.length == 0 || check == false) {
        return '';
    }
    else {
        let ind = chars.indexOf(chars.find(x => chars.indexOf(x) === chars.lastIndexOf(x)));
        return s[ind];
    }
}
console.log(firstNonRepeatingLetter('a'), 'a');
console.log(firstNonRepeatingLetter('stress'), 't');
console.log(firstNonRepeatingLetter('moonmen'), 'e');
console.log(firstNonRepeatingLetter("Go hang a salami, I'm a lasagna hog!"), ",");
console.log(firstNonRepeatingLetter('sTreSS'), 'T');
console.log(firstNonRepeatingLetter('abba'), 'empty');
console.log(firstNonRepeatingLetter(''), 'empty');