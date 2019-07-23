function bouncer(arr) {
    // Don't show a false ID to this bouncer.
    return arr.filter(x => Boolean(x));
}

console.log(bouncer([7, "ate", "", false, 9]));
console.log(bouncer(["a", "b", "c"]));
console.log(bouncer([false, null, 0, NaN, undefined, ""]));
console.log(bouncer([1, null, NaN, 2, undefined]));