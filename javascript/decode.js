function decodeMessage(message) {
    const vowels = { 4: 'a', 3: 'e', 1: 'i', 0: 'o', 2: 'u', 5: 'y' };
    var decoded = [];
    message.split('').map(x => { decoded.push(vowels[x] || x) });
    return decoded.join('');
}

console.log(decodeMessage("th1s 1s 4 t3st. th1s 1s 0nl5 4 t3st. 1f th1s w3r3 4 r34l m3ss4g3, 502 w021d g3t s0m3th1ng m34n1ngf2l."));