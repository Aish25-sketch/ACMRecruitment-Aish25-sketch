# String Reversal Methods

We implemented **two methods** to reverse a string without using built-in functions.

### 1. Iterative Method
- Use two pointers (start and end of the string).
- Swap characters until the middle of the string is reached.

### 2. Recursive Method
- Base case: if the string length is 0 or 1, return it.
- Otherwise, reverse the rest of the string and append the first character at the end.

### Example:
Input: 'ACM Recruitment'  
Output: 'tnemtiurceR MCA'
