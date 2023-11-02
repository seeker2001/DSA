"""
Leetcode : 1
Problem Statement: Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the
target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target.
Otherwise, we will return {-1, -1}.

Brute Force Solution:
1. Using two nested loop find the required pair
 
Time Complexity -> O(N ^ 2) Space Complexity -> O(1)

Optimized Solution:
1. Using Hashmap 

Time Complexity -> O(N) Space Complexity -> O(N)
"""
from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            mp[num] = i
        for i, num in enumerate(nums):
            if target - num in mp and mp[target - num] != i:
                return [i, mp[target - num]]
