// You ask a small girl,"How old are you?" She always says, "x years old",
//  where x is a random number between 0 and 9.

// Write a program that returns the girl's age (0-9) as an integer.

// Assume the test input string is always a valid string. For example,
//  the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

function extractAge(input) {
    // Extract the first character of the string, which is a digit
    const ageChar = input[0];

    // Convert the character to an integer and return
    return parseInt(ageChar, 10);
}

const input1 = "1 year old";
const input2 = "5 years old";

const age1 = extractAge(input1);
const age2 = extractAge(input2);

console.log("Extracted Age 1: ", age1);
console.log("Extracted Age 2: ", age2);