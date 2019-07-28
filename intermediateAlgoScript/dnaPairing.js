function pairElement(str) {
    let at = 'AT',
        gc = 'GC';
    return str.split('').map(x => {
        if (at.includes(x)) {
            if (at.indexOf(x) == 1) {
                return at.split('').reverse();
            }
            return at.split('');
        } else {
            if (gc.indexOf(x) == 1) {
                return gc.split('').reverse();
            }
            return gc.split('');
        }
    });
}

console.log(pairElement("GCG"));
console.log(pairElement("ATCGA"));
console.log(pairElement("TTGAG"));
console.log(pairElement("CTCTA"));