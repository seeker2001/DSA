"""
Leetcode : 18
Problem Statement: Given an array of N integers, your task is to find unique quads that
add up to give a target value. In short, you need to return an array of all the unique
quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given
target.

Brute Force Approach:
1. Try all possible quadruplets and compare their sum to target.
2. If the sum is equal to target, add the quadruplet to the result.

Time Complexity -> O(N^4) Space Complexity -> O(1)

Optimal Approach (Using Sorting):
1. Sort the array.
2. Pick first 2 elements of quadruplet in the outer loops and other 2 elements in a loop
using 2 pointers (as the elements are sorted).

Key Points -> We only need unique quadruplets so make sure to skill all duplicate ones.

Time Complexity -> O(N^3) Space Complexity -> O(1)
"""
from typing import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                pairTarget = target - nums[i] - nums[j]
                while l < r:
                    pairSum = nums[l] + nums[r]
                    if pairSum > pairTarget:
                        r -= 1
                    elif pairSum < pairTarget:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] + nums[r] == pairTarget:
                            l += 1
        return res
