function makeClass() {
    "use strict";
    /* Alter code below this line */
    class Thermostat {
        constructor(F) {
            this.degree = F;
        }
        get temperature() {
            return 5 / 9 * (this.degree - 32);
        }

        set temperature(C) {
            return this.degree = C * 9.0 / 5 + 32;
        }
    }
    /* Alter code above this line */
    return Thermostat;
}
const Thermostat = makeClass();
const thermos = new Thermostat(76); // setting in Fahrenheit scale
let temp = thermos.temperature
console.log(temp); // 24.44 in C
thermos.temperature = 26;
console.log(temp = thermos.temperature); // 26 in C