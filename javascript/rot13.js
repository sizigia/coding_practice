function rot13(str) { // LBH QVQ VG!
  let alphabet = "abcdefghijklmnopqrstuvwxyz";
  let aLen = alphabet.length;
  let index = (letter) => {
    let initial = alphabet.indexOf(letter) + 13;
    if (initial >= 0 && initial <= 25) {
      return initial;
    }
    else {
      do {
        initial -= aLen;
      } while (initial > 25);
      return initial;
    }
  }

  let replaceLetter = char => {
    if (char.match(/[a-z]/g)) {
      return alphabet[index(char)].toUpperCase();
    }
    else if (char.match(/[A-Z]/g)) {
      let lowChar = char.toLowerCase();
      return alphabet[index(lowChar)].toUpperCase();
    }
    else {
      return char;
    }
  };
  return str.split("").map(replaceLetter).join("");
}

// Change the inputs below to test
console.log(rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT."));