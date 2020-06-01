function truncateString(str, num) {
    // Clear out that junk in your trunk
    if (str.length > num) {
        return str.split('').splice(0, num).join('') + "...";
    }
    return str;
}

console.log(truncateString("A-tisket a-tasket A green and yellow basket", 8));
console.log(truncateString("Peter Piper picked a peck of pickled peppers", 11));
console.log(truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length));
truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length + 2);
console.log(truncateString("A-", 1));
console.log(truncateString("Absolutely Longer", 2));