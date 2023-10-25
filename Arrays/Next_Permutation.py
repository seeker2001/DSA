"""
Leetcode : 31
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given
array into the lexicographically next greater permutation of numbers.If such an arrangement
is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending
order).

Brute Force Solution: 
1. Generate all the possible permutations of the array in lexicographical order and while 
finding current permutation keep track of the previous one.
2. Now if the previous permutation is the current array then the current permutation would
be the required one (next permutation).
3. If we don't find such case then we will simply return the array rearranged in lowest 
possible order.

Time Complexity -> O(n! * n) Space complexity -> O(n)

Optimized Solution:
1. Find the break-point, i: Break-point means the first index i from the back of the given 
array where arr[i] becomes smaller than arr[i+1].
For example, if the given array is {2,1,5,4,3,0,0}, the break-point will be index 1(0-based 
indexing). Here from the back of the array, index 1 is the first index where arr[1] i.e. 1 
is smaller than arr[i+1] i.e. 5. To find the break-point, using a loop we will traverse the 
array backward and store the index i where arr[i] is less than the value at index (i+1) i.e. 
arr[i+1].

2. If such a break-point does not exist i.e. if the array is sorted in decreasing order, the 
given permutation is the last one in the sorted order of all possible permutations. So, the 
next permutation must be the first i.e. the permutation in increasing order.So, in this case,
we will reverse the whole array and will return it as our answer.

3. If a break-point exists:
Find the smallest number i.e. > arr[i] and in the right half of index i(i.e. from index i+1 
to n-1) and swap it with arr[i].
Reverse the entire right half(i.e. from index i+1 to n-1) of index i. And finally, return 
the array.

Time Complexity -> O(n) Space Complexity -> O(1)
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            # condition for break-point
            if nums[i] < nums[i + 1]:
                j = len(nums) - 1
                while nums[i] >= nums[j]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                break
            i -= 1

        # reverse the part to right of i
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
