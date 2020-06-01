const factorial = require('./factorial')

describe(`Basic tests`, () => {
    it(`factorial(0)`, () => {
        expect(factorial(0)).toEqual(1);
    });
    it(`factorial(1)`, () => {
        expect(factorial(1)).toEqual(1);
    });
    it(`factorial(2)`, () => {
        expect(factorial(2)).toEqual(2);
    });
    it(`factorial(3)`, () => {
        expect(factorial(3)).toEqual(6);
    });
});