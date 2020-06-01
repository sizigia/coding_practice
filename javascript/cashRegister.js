/** JavaScript Algorithms and Data Structures Projects: Cash Register
Design a cash register drawer function checkCashRegister() that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.

cid is a 2D array listing available currency.

The checkCashRegister() function should always return an object with a status key and a change key.

Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less than the change due, or if you cannot return the exact change.

Return {status: "CLOSED", change: [...]} with cash-in-drawer as the value for the key change if it is equal to the change due.

Otherwise, return {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted in highest to lowest order, as the value of the change key.
-_-_-_-_-_-_-
Currency Unit	Amount
Penny	$0.01 (PENNY)
Nickel	$0.05 (NICKEL)
Dime	$0.1 (DIME)
Quarter	$0.25 (QUARTER)
Dollar	$1 (DOLLAR)
Five Dollars	$5 (FIVE)
Ten Dollars	$10 (TEN)
Twenty Dollars	$20 (TWENTY)
One-hundred Dollars	$100 (ONE HUNDRED)
 */

function checkCashRegister(price, cash, cid) {
  const currencyUnit = { PENNY: 0.01, NICKEL: 0.05, DIME: 0.1, QUARTER: 0.25, ONE: 1, FIVE: 5, TEN: 10, TWENTY: 20, 'ONE HUNDRED': 100, }
  let changeAmount = cash - price;
  let charge = [];
  function parseCash(changeAmount) {
    let change = {};

    let q = parseFloat((changeAmount % 0.25).toFixed(2));
    let r = parseFloat((changeAmount % 1).toFixed(2));
    changeAmount -= change.QUARTER = r - q;

    let a = parseFloat((changeAmount % 0.1).toFixed(2));
    if (a < 0.05) {
      changeAmount -= change.PENNY = a;
    } else if (a == 0.05) {
      changeAmount -= change.NICKEL = a;
    } else if (a > 0.05) {
      change.NICKEL = 0.05;
      change.PENNY = a - 0.05;
      changeAmount -= a;
    }

    let b = parseFloat((changeAmount % 1).toFixed(2));
    changeAmount -= change.DIME = b;

    let c = parseFloat((changeAmount % 10).toFixed(2));
    if (c < 5) {
      changeAmount -= change.ONE = c;
    } else if (c == 5) {
      changeAmount -= change.FIVE = c;
    } else if (c > 5) {
      change.FIVE = 5;
      change.ONE = c - 5;
      changeAmount -= c;
    }

    changeAmount -= change.TWENTY = changeAmount - (changeAmount % 20);
    change.TEN = parseFloat(changeAmount.toFixed(2));

    return change;
  }

  let change = parseCash(changeAmount);
  for (let i in change) {
    charge.push(change[i]);
  }

  cid.map(x => {
    console.log(x);
    x.reduce((x, z) => {
      console.log(z);
    });
  });

  console.log(change, charge);
}
console.log(checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]))
//console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));