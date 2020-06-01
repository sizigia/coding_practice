function sumFibs(num) {
    let sum = 1;
    let fi = 1;
    const fib = {
        f2: 1,
        f1: 1,
    }

    while (fi <= num) {
        if (fi % 2 != 0) {
            sum += fi;
        }
        fi = fib['f2'] + fib['f1'];
        fib['f2'] = fib['f1'];
        fib['f1'] = fi;
    }

    return sum;
}

console.log(sumFibs(10));
console.log(sumFibs(1000));
console.log(sumFibs(4000000));
console.log(sumFibs(4));
console.log(sumFibs(75024));
console.log(sumFibs(75025));