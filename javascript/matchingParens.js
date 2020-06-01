/*
Write a function that, given a sentence like the one above, 
along with the position of an opening parenthesis, 
finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis), 
the output should be 79 (position of the last parenthesis).

https://www.interviewcake.com/question/python/matching-parens
*/

/*
Problem:
find a closing parenthesis from an opening one with known index

Structure of solution:
function takes two arguments,
1. string
2. position of opening parenthesis
returns index of last parenthesis

V1 Algorithm:
check if indeed you have a parenthesis in the given index, (if not return error)
if so, 
    get the last index of a parenthesis on the string,
    that's going to be the matching parenthesis

V1 Logic is wrong, because it will fail to get the matching parenthesis
if the given index does not correspond to the first parenthesis on the string.
*/

test = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

// function matchingParens(str, ind) {
//     if (str[ind] == '(') {
//         return str.lastIndexOf(')');
//     }
//     return console.error("We couldn't find your parenthesis.");

// }

console.log(matchingParens(test, 10));



/**
V2 Algo:
    using a stack to track which brackets/phrases/etc are "open" as you go
    have an array that keeps index of the parentheses after the first
*/

function matchingParens(str, ind) {
    let len = str.length - 1;
    let string = str.slice(ind + 1, len).split("");
    let closingParens = string.reduce(function (parens, v, i) { if (v === ")") parens.push(ind + 1 + i); return parens; }, []).reverse();
    string.reduce(function ([], v) {
        if (v === "(") {
            closingParens.pop();
        }
        return closingParens;
    });
    return closingParens.pop();
}