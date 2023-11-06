"""
Leetcode:128
Problem Statement: You are given an array of 'N' integers. You need to find the length 
of the longest sequence which contains the consecutive elements.

Brute Force Approach:
1. Traverse the array and try to find the LCS starting from the current element.
2. Find the longest sequence and return its length.

Time Complexity -> O(N^2) Space Complexity -> O(1)

Optimal Approach 1:
1. Sort the array.
2. Traverse the array and find the LCS.

Time Complexity -> O(NlogN) Space Complexity -> O(1)

Optimal Approach 2:
1. Add all the elements of array into set.
2. Now traverse the array and for each element check whether the longest sequence it can 
be part of starts with that element
    (a) Check (cur - 1) is in the set 
        (i) if it is then continue
        (ii) if it is not then it means the sequence will start from current element and
             find the longest sequence starting from there.

Time Complexity -> O(N) Space Complexity -> O(1) 
"""
from typing import *


class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
