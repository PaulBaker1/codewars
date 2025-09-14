"""
 * 
 *  Instructions
 *  Write a function that takes a single non-empty string of only lowercase and 
 *  uppercase ascii letters (word) as its argument, and returns an ordered list 
 *  containing the indices of all capital (uppercase) letters in the string.
 *  Example (Input --> Output)
 *  "CodEWaRs" --> [0,3,4,6]
 */
"""

def capitals(word):
    # Initialize an empty list to store the indices of capital letters
    result = []

    # Iterate through each character in the input string
    for i, char in enumerate(word):
        # Check if the current character is an uppercase letter
        if char.isupper():
            # Append the index of the capital letter to the result list
            result.append(i)
    
    return result

# Example usage
word = "CodEWaRs"
capitals_indices = capitals(word)
print(capitals_indices)