
// You ask a small girl,"How old are you?" She always says, "x years old",
//  where x is a random number between 0 and 9.

// Write a program that returns the girl's age (0-9) as an integer.

// Assume the test input string is always a valid string. For example,
//  the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

public class Main {
    public static int extractAge(String input) {
        // Extract the first character of the string, which is a digit
        char ageChar = input.charAt(0);
        
        // Convert the character to an integer and return it
        return Character.getNumericValue(ageChar);
    }

    public static void main(String[] args) {
        String input1 = "1 year old";
        String input2 = "5 years old";

        int age1 = extractAge(input1);
        int age2 = extractAge(input2);

        System.out.println("Extracted Age 1: " + age1); // Output: Extacted Age 1: 1
        System.out.println("Extracted Age 2: " + age2); // Output: Extracted Age 2: 5
    }
}
