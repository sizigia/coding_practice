function sumPrimes(num) {
    function prime(num) {
        let divisors = 1;
        for (let i = 2; i <= num; i++) {
            if (num % i === 0) {
                divisors++;
                if (divisors > 2) {
                    return false;
                }
            }
        }
        return true;
    }
    let sum = 0;
    if ([0, 1, 2].includes(num)) {
        return num;
    } else {
        for (let i = 2; i <= num; i++) {
            if (prime(i)) {
                sum += i;
            }
        }
    }
    return sum;
}

console.log(sumPrimes(10));
console.log(sumPrimes(977));


