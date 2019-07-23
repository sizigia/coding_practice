function repeatStringNumTimes(str, num) {
    // repeat after me
    let repeated = '';
    if (num < 0) {
        return "";
    }
    for (let i = 1; i <= num; i++) {
        repeated += str;
    }
    return repeated;
}

console.log(repeatStringNumTimes("*", -3));