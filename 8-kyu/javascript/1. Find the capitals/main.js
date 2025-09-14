/**
 * 
 *  Instructions
 *  Write a function that takes a single non-empty string of only lowercase and 
 *  uppercase ascii letters (word) as its argument, and returns an ordered list 
 *  containing the indices of all capital (uppercase) letters in the string.
 *  Example (Input --> Output)
 *  "CodEWaRs" --> [0,3,4,6]
 */

function capitals(word) {
    // Initialize an empty array to store the indices of capital letters
    const result = [];

    // Iterate through each character in the input string
    for (let i = 0; i < word.length; i++) {
        // Check if the current character is an uppercase letter
        if (word[i] === word[i].toUpperCase()) {
            // Append the index of the capital letter to the result array
            result.push(i);
        }
    }
    return result;
}

// Example
const word = "CodEWaRs";
const capitalIndices = capitals(word);
console.log(capitalIndices);