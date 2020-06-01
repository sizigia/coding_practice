function convertToRoman(num) {
  const conv = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }
  var rom = {};

  num -= rom.one = num % 10;
  num -= rom.ten = num % 100;
  num -= rom.hundred = num % 1000;
  rom.thousand = num;

  num = Object.values(rom).reverse().map(x => {
    var i, r;
    if (x == rom.one) {
      i = 0;
    } else if (x == rom.ten) {
      i = 1;
    } else if (x == rom.hundred) {
      i = 2;
    } else if (x == rom.thousand) {
      i = 3;
    }
    switch (x) {
      case (1 * 10 ** i):
      case (2 * 10 ** i):
      case (3 * 10 ** i):
        r = x / (10 ** i);
        return (conv[10 ** i]).repeat(r);
      case (4 * 10 ** i):
        return conv[10 ** i] + conv[5 * 10 ** i];
      case (5 * 10 ** i):
        return conv[5 * 10 ** i];
      case (6 * 10 ** i):
      case (7 * 10 ** i):
      case (8 * 10 ** i):
        r = (x - (5 * 10 ** i)) / (10 ** i);
        return conv[5 * 10 ** i] + (conv[10 ** i]).repeat(r);
      case (9 * 10 ** i):
        return conv[10 ** i] + conv[10 ** (i + 1)];
      case (10 ** i):
        return conv[10 ** i];
    }
  }).join('');
  console.log(num);
  return num;
};

convertToRoman(29);

/*Object.entries()
Object.keys()
Object.values()
*/