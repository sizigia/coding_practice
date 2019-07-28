function pairElement(str) {
    let base = [['A', 'T'], ['C', 'G']];
    return str.split('').map(x => {
        switch (x) {
            case 'A':
                return ['A', 'T'];
            case 'T':
                return ['T', 'A'];
            case 'G':
                return ['G', 'C'];
            case 'C':
                return ['C', 'G'];
        }
    })
}

console.log(pairElement("GCG"));
console.log(pairElement("ATCGA"));
console.log(pairElement("TTGAG"));
console.log(pairElement("CTCTA"));