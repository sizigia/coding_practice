function convertHTML(str) {
    const entities = {
        '<': '&lt;',
        '>': '&gt;',
        '&': '&amp;',
        '\"': '&quot;',
        '\'': '&apos;',
    }

    let converted = str.split('').map(x => entities[x] ? entities[x] : x).join('');

    return converted;
}

console.log(convertHTML("Dolce & Gabbana"))
console.log(convertHTML("Hamburgers < Pizza < Tacos"))
console.log(convertHTML("Sixty > twelve"))
console.log(convertHTML('Stuff in "quotation marks"'))
console.log(convertHTML("Schindler's List"))
console.log(convertHTML("<>"))
console.log(convertHTML("abc"))