function mutation(arr) {
    const separate = (word) => {   
        return word.toLowerCase().split('');        
    }
    let letters = separate(arr[0]);
    let check = separate(arr[1]);
    for (let l in check) {
        if (letters.indexOf(check[l]) === -1) {
            return false;
        }
    }
    return true;
}

console.log(mutation(["Hello", "hey"]));