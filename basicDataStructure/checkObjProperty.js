let users = {
    Alan: {
        age: 27,
        online: true
    },
    Jeff: {
        age: 32,
        online: true
    },
    Sarah: {
        age: 48,
        online: true
    },
    Ryan: {
        age: 19,
        online: true
    }
};

function isEveryoneHere(obj) {
    // change code below this line
    let names = ['Alan', 'Jeff', 'Sarah', 'Ryan'];
    for (let i = 0; i < names.length; i++) {
        console.log(names[i]);
        if (names[i] in obj == false) {
            return false;
        }
    }
    return true;
    // change code above this line
}

console.log(isEveryoneHere(users));