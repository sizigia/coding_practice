function squareDigits(num) {
    const sqr = (n) => (parseInt(n, 10)) ** 2
    return parseInt(num.toString().split('').map(sqr).join(''));
}

squareDigits(9119);