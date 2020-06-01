function productFib(prod) {
    let fib = {
        fn2: 0,
        fn1: 1,
        fn: 0,
        prod: 0,
    }
    while (fib.prod <= prod) {
        fib.fn = fib.fn1 + fib.fn2;
        fib.fn2 = fib.fn1;
        fib.fn1 = fib.fn;
        fib.prod = fib.fn2 * fib.fn1;
        if (fib.prod == prod) {
            return [fib.fn2, fib.fn1, true];
        }
    }
    return [fib.fn2, fib.fn1, false];
}

console.log(productFib(4895), [55, 89, true])
console.log(productFib(5895), [89, 144, false])
console.log(productFib(74049690), [6765, 10946, true])
console.log(productFib(84049690), [10946, 17711, false])
console.log(productFib(193864606), [10946, 17711, true])
console.log(productFib(447577), [610, 987, false])
console.log(productFib(602070), [610, 987, true])