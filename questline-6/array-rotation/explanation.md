# Array Rotation

## Problem
Given an integer array 'num', rotate the array to the right by 'k' steps, where 'k' is non-negative.

## Solution Approach
1. Normalize 'k' using 'k=k%len(nums)' (in case 'k'>size of array)
2. Slice the array into two parts:
   - Last 'k' elements.
   - First 'len(nums)-k' elements.
3. Link them to form the rotated array.

### Example
Input: num= [1,2,3,4,5,6,7],k=3  
Output: [5,6,7,1,2,3,4]
