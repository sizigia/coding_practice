decodeMorse = function (morseCode) {
  const morseLetter = (letter) => MORSE_CODE[letter] || letter;
  return morseCode.trim().split(' ').map(morseLetter).join('').replace(/\s+/g, ' ');
}

console.log(decodeMorse('.... . -.--   .--- ..- -.. .'));
