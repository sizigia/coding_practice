function checkCashRegister(price, cash, cid) {
    const currencyUnit = { PENNY: 0.01, NICKEL: 0.05, DIME: 0.1, QUARTER: 0.25, ONE: 1, FIVE: 5, TEN: 10, TWENTY: 20, 'ONE HUNDRED': 100, }
    let changeAmount = cash - price;
    let change = [];
    let minCash = 0;
    cid.reverse().map(x => {
        x.reduce((a, b) => {
            if (changeAmount >= currencyUnit[a]) {
                minCash += b;
                if (changeAmount > b) {
                    changeAmount -= b;
                    change.push([a, b]);
                } else if (changeAmount <= b) {
                    let base = Math.floor(changeAmount / currencyUnit[a]);
                    let sub = (currencyUnit[a] * base);
                    changeAmount -= sub;
                    changeAmount = changeAmount.toFixed(2);
                    change.push([a, sub]);
                }
            }
            
        });
    })
    //console.log(minCash, changeAmount, change);

    if (minCash < changeAmount) {
        return { status: 'INSUFFICIENT FUNDS', change: [] };
    }
    else if (minCash == (cash - price) && changeAmount == 0) {
        return { status: 'CLOSED', change: cid.reverse() };
    }
    else if ((minCash - (cash - price)) > 0 && changeAmount == 0) {
        return { status: 'OPEN', change: change };
    }
}

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));