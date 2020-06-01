// the global variable
var globalTitle = " Winter Is   Coming";

// Add your code below this line
function urlSlug(title) {
  return title.toLowerCase().split(/\W/g).filter(x => x.match(/[a-z]/g)).join("-");
}
// Add your code above this line

var winterComing = urlSlug(globalTitle); // Should be "winter-is-coming"
console.log(winterComing);