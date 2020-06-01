function diffArray(arr1, arr2) {
  var newArr = [].concat(filteredItems(arr1, arr2),filteredItems(arr2, arr1)).sort();
  return newArr;

  function filteredItems(arr, otherArr) {
    return arr.filter(x => {
      if ((arr.includes(x) && otherArr.includes(x)) === false) {
        return x;
      }
    });
  }
}

console.log(diffArray(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]));