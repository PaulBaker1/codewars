import java.util.Arrays;

/**
 * 
 *  Instructions
 *  Write a function that takes a single non-empty string of only lowercase and 
 *  uppercase ascii letters (word) as its argument, and returns an ordered list 
 *  containing the indices of all capital (uppercase) letters in the string.
 *  Example (Input --> Output)
 *  "CodEWaRs" --> [0,3,4,6]
 */

 public class Main {
    public static int[] capitals(String s) {
        // Create an array to store the indices of capital Letters
        int[] result = new int[s.length()];

        // Initialize a counter for the index in the result array
        int index = 0;

        // Iterate through each character in the input string
        for (int i = 0; i < s.length(); i++) {
            // Check if the current character is an uppercase letter
            if (Character.isUpperCase(s.charAt(i))) {
                // Store the index of the capital letter in the result array
                result[index++] = i;
            }
        }

        // Create a new array to store only the valid indices
        int[] findResult = new int[index];
        System.arraycopy(result, 0, findResult, 0, index);

        return findResult;
    }
    public static void main(String[] args) {
        String word = "CodEWaRs";
        int[] capitalsIndices = capitals(word);
        System.out.println(Arrays.toString(capitalsIndices));
    }
 }