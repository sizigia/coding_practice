function checkCashRegister(price, cash, cid) {
    const currencyUnit = { PENNY: 0.01, NICKEL: 0.05, DIME: 0.1, QUARTER: 0.25, ONE: 1, FIVE: 5, TEN: 10, TWENTY: 20, 'ONE HUNDRED': 100, }
    let changeAmount = cash - price;
    let charge = [];
    let minCash = 0;


    function parseCash(changeAmount) {
        let change = {};

        let q = parseFloat((changeAmount % 0.25).toFixed(2));
        let r = parseFloat((changeAmount % 1).toFixed(2));
        changeAmount -= change.QUARTER = r - q;

        let a = parseFloat((changeAmount % 0.1).toFixed(2));
        if (a < 0.05 && a != 0) {
            changeAmount -= change.PENNY = a;
        } else if (a == 0.05) {
            changeAmount -= change.NICKEL = a;
        } else if (a > 0.05) {
            change.NICKEL = 0.05;
            change.PENNY = a - 0.05;
            changeAmount -= a;
        }

        let b = parseFloat((changeAmount % 1).toFixed(2));
        if (b != 0) { changeAmount -= change.DIME = b; }

        let c = parseFloat((changeAmount % 10).toFixed(2));
        if (c < 5 && c != 0) {
            changeAmount -= change.ONE = c;
        } else if (c == 5) {
            changeAmount -= change.FIVE = c;
        } else if (c > 5) {
            change.FIVE = 5;
            change.ONE = c - 5;
            changeAmount -= c;
        }

        if (changeAmount != 0) {
            changeAmount -= change.TWENTY = changeAmount - (changeAmount % 20);
            change.TEN = parseFloat(changeAmount.toFixed(2));
        }

        return change;
    }

    let change = parseCash(changeAmount);


    cid.map(x => {
        x.reduce((d, e) => {
            if (typeof d == 'string') {
                if (change[d] <= changeAmount) {
                    minCash += e;
                }
            }
        });
    });
    console.log(Object.entries(change).sort(cid));

    
}

//console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
console.log(checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]))
//console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));
console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));