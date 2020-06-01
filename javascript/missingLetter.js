function fearNotLetter(str) {
    let charCodes = str.split('').map(x => x.charCodeAt(0));

    for (let i = 0; i < charCodes.length; i++) {
        if (charCodes[i] + 1 !== charCodes[i + 1]) {
            if (charCodes.length == 26) {
                return undefined;
            }
            return String.fromCharCode(charCodes[i] + 1)
        }
    }
    return undefined;
}

console.log(fearNotLetter("abce"));
console.log(fearNotLetter("abcdefghjklmno"));
console.log(fearNotLetter("stvwx"));
console.log(fearNotLetter("bcdf"));
console.log(fearNotLetter("abcdefghijklmnopqrstuvwxyz"));