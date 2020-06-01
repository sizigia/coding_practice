function findLongestWordLength(str) {
    let wordLen = str.split(' ').map(x => x.length);
    return Math.max(...wordLen);
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"));