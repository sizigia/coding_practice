function convertToRoman(num) {
  const conv = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }
  var rom = {};

  num -= rom.one = num % 10;
  num -= rom.ten = num % 100;
  num -= rom.hundred = num % 1000;
  rom.thousand = num;

  num = Object.values(rom).reverse().map(x => {
    for (let i in conv) {
      if (x > i && x + i < 4*i) { return conv[1].repeat(x) }
      else if (x + 1 == i) { return conv[1] + conv[i] }
      else if (x == i) { return conv[i] }
      else if (x > 5 && x + 1 < i - 1) { let r = x - 5; return conv[5] + conv[1].repeat(r) }
      else if (x + 1 == 10) { return conv[1] + conv[i] }
      else if (x == 10) { return conv[10] }
      else if (x > 10 && x + 10 < 50) { return conv[10].repeat(x / 10) }
      else if (x + 10 == 50) { return conv[10] + conv[50] }
    }
  }).join('');

  console.log(Object.values(conv));
  console.log(num);
  return;
};



convertToRoman(9);

/*Object.entries()
Object.keys()
Object.values()
*/