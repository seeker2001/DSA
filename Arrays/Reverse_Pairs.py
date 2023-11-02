"""
Leetcode : 493
Problem Statement: Given an array of numbers, you need to return the count of reverse 
pairs.Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].

Solutions -> Similar to Count Inversions

Optimal Solution (Using Merge Sort):
1. The only change here will be that in merge method we will not simultaneously merge and
count ways but we will do it in a different loop.

Time Complexity -> O(NlogN) Space Complexity -> O(1)
"""
from typing import *


class Solution:
    def merge(self, left, right, nums, res):
        nl, nr = len(left), len(right)
        i, j, k = 0, 0, 0
        while i < nl and j < nr:
            if left[i] <= 2 * right[j]:
                i += 1
            else:
                res[0] += nl - i
                j += 1
        i, j = 0, 0
        while i < nl and j < nr:
            if left[i] > right[j]:
                nums[k] = right[j]
                j += 1
            else:
                nums[k] = left[i]
                i += 1
            k += 1
        while i < nl:
            nums[k] = left[i]
            i += 1
            k += 1
        while j < nr:
            nums[k] = right[j]
            j += 1
            k += 1
        return nums

    def mergeSort(self, nums, res):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left, right = self.mergeSort(nums[:mid], res), self.mergeSort(nums[mid:], res)
        return self.merge(left, right, nums, res)

    def reversePairs(self, nums: List[int]) -> int:
        res = [0]
        self.mergeSort(nums, res)
        return res[0]
