// Write a function that takes two numbers and returns their sum?
    //input
        // only one input?
        // Can I assume valid input?
        // number, int, float, double?


// write a functions that takes a string and returns counts of each char in the string
// hello => {h: 1}
// "" => {}
// Hello => {h: 1}
// Hello World! => only letters (no spaces and symbols)

function charCount(str) {
    // declare object
    let result = {};

    // loop through string
    for (let i = 0; i < str.length; i++) {
        //lowercase
        let char = str[i].toLowerCase();

        //check alphanumeric
        if (/[a-z0-9]/.test(char)) {
            // if value in object, increment count
            result[char] ? result[char] += 1 : result[char] = 1;
        }
    }
    //return object
    return result;
}

console.log(charCount('hello'))