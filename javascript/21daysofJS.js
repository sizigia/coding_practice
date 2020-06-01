var navigation = {
    x: -2,
    y: 4,
    z: 7,
    speed: "raaaaid"
};

function setSpeed(speed) {
    let navSpeed = parseInt(speed);
    switch (Math.sign(navSpeed)) {
        case 0:
        case 1:
            navigation.speed = navSpeed;
            break;
        case -1:
            navigation.speed = 0;
            break;
    }
}

console.log(setSpeed("12"));
console.log(navigation.speed);
