function telephoneCheck(str) {
  if (str.match(/^[1]?(-|\s)?(\(\d{3}\)|\d{3})(-|\s)?\d{3}(-|\s)?\d{4}$/g)) {
    return true;
  }
  return false;
}

let number = "(555) 555-5555";
console.log(telephoneCheck("555-555-5555"));
console.log(telephoneCheck(number));
console.log(telephoneCheck("555-555-5555"));
console.log("false:" + telephoneCheck("555-5555"));