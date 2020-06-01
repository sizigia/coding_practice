function titleCase(str) {
    let titled = str.toLowerCase().split(' ').map(x => x[0].toUpperCase() + x.substring(1)).join(' ');
    return titled;
}

console.log(titleCase("I'm a little tea pot"));
console.log(titleCase("sHoRt AnD sToUt"));
console.log(titleCase("HERE IS MY HANDLE HERE IS MY SPOUT"));
