function towerBuilder(nFloors) {
    let tower = [], i = 0;
    while (tower.length < nFloors) {
        tower.push(' '.repeat(nFloors - 1 - i) + '*'.concat('**'.repeat(i)) + ' '.repeat(nFloors - 1 - i));
        i++;
    }
    return tower;
}
console.log(towerBuilder(1), ["*"]);
console.log(towerBuilder(2), [" * ", "***"]);
console.log(towerBuilder(3), ["  *  ", " *** ", "*****"]);