function romanos(num) {
  const romValues = [{ 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }];
  const romKeys = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];
  let digits = num.toString().split('');
  console.log(romValues[digits[1].toString()]);

  return;
}

romanos(2563);