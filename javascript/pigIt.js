function pigIt(str) {
    let pig = [];
    str.split(' ').map(x => {
        if (x.match(/\W/gi)) {
            return pig.push(x);
        }
        let word = x.split('');
        word.push(word.shift());
        pig.push(word.join('').concat('ay'));
    });
    return pig.join(' ');
}

// console.log(pigIt('Pig latin is cool'), 'igPay atinlay siay oolcay')
// console.log(pigIt('This is my string'), 'hisTay siay ymay tringsay')
console.log(pigIt("O tempora o mores !"), 'Oay emporatay oay oresmay !')
console.log(pigIt("Quis custodiet ipsos custodes ?"), 'uisQay ustodietcay psosiay ustodescay ?')