function iqTest(numbers) {
    let arrNum = numbers.split(' ');
    var o = 0, e = 0;
    arrNum.map(x => {
        (x % 2 == 0) ? e += 1 : o += 1;
    })
    if (e > o) {
        let odd = arrNum.find(x => x % 2 != 0);
        return arrNum.indexOf(odd) + 1;
    }
    else {
        let even = arrNum.find(x => x % 2 == 0);
        return arrNum.indexOf(even) + 1;
    }
}


console.log(iqTest("2 4 7 8 10"), 3);
console.log(iqTest("1 2 2"), 1);
console.log(iqTest("5 3 2"), 3)
console.log(iqTest("43 28 1 91"), 2)
console.log(iqTest("79 27 77 57 37 45 27 49 65 33 57 21 71 19 75 85 65 61 23 97 85 9 23 1 9 3 99 77 77 21 79 69 15 37 15 7 93 81 13 89 91 31 45 93 15 97 55 80 85 83"), 48)
console.log(iqTest("9 31 27 93 17 77 75 9 9 53 89 39 51 99 5 1 11 39 27 49 91 17 27 79 81 71 37 75 35 13 93 4 99 55 85 11 23 57 5 43 5 61 15 35 23 91 3 81 99 85 43 37 39 27 5 67 7 33 75 59 13 71 51 27 15 93 51 63 91 53 43 99 25 47 17 71 81 15 53 31 59 83 41 23 73 25 91 9"), 32)