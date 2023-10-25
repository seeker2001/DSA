"""
Leetcode: 75
Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to 
in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) 
and constant space)

Brute Force Solution:
1. Count the number of 0s, 1s and 2s in the array.
2. Just store these 0s, 1s and 2s in order in the array (as we already now their count).

Time Complexity -> O(n) Space Complexity -> O(1)

Optimized Solution:
1. Use a three pointer approach to sort this array (low, mid, high).

2. The steps will be the following:

First, we will run a loop that will continue until mid <= high.
There can be three different values of mid pointer i.e. arr[mid]
(a) If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. 
Now the subarray from index 0 to (low-1) only contains 0.
(b) If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will 
point to 1 as it should according to the rules.
(c) If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the 
subarray from index high+1 to (n-1) only contains 2.
In this step, we will do nothing to the mid-pointer as even after swapping, the subarray 
from mid to high(after decrementing high) might be unsorted. So, we will check the value of 
mid again in the next iteration.

3. Finally, our array should be sorted.
4. The arr[0….low-1] contains 0, arr[low….mid-1] contains 1 and arr[high+1….n-1] contains 2.
[Extreme right part], n = size of the array
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
