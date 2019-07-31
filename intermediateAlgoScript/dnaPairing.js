function pairElement(str) {
    let base = ['AT', 'CG'];
    let paired = [];

    str.split('').map(bUnit => {
        base.map(x => {
            if (x.indexOf(bUnit) == 0) {
                paired.push(x.split(''));
            }
            else if (x.indexOf(bUnit) == 1) {
                paired.push(x.split('').reverse())
            }
        })
    });
    return paired;
}

console.log(pairElement("GCG"));
console.log(pairElement("ATCGA"));
console.log(pairElement("TTGAG"));
console.log(pairElement("CTCTA"));