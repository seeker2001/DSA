"""
Leetcode : 53
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at 
least one number) which has the largest sum and returns its sum.

Brute Force Solution:
1. Try all possible subarray sum and return the maximum one.

Time Complexity -> O(n ^ 2) Space Complexity -> O(1)

Optimized Solution:
Kadane's Algorithm ::
1. Keep track of two things while iterating the array: current subarray sum(curSum) and 
maximum subarray sum that we have found till now (maxSum).
2. If curSum >= 0: continue, otherwise reinitialize the curSum = 0

Time Complexiyt -> O(n) Space Complexity -> O(1)
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curSum, maxSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum
