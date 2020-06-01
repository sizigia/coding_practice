function sumAll(arr) {
  return arr.reduce((x, y) => {
    var sum1 = x + y;
    var sum2 = 0;
    if (x < y) {
      while (x < y - 1) {
        x++;
        sum2 += x;
      }
    }
    else if (x > y) {
      while (x - 1 > y) {
        x--;
        sum2 += x;
      }
    }
    return sum1 + sum2;
  });
}

console.log(sumAll([4, 1]));