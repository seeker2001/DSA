"""
Leetcode : 287
Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. 
Assuming there is only one duplicate number, your task is to find the duplicate number.

Brute Force Approach:
1. Using 2 nested loops find the freq of each element.
2. The element which has a frequency of 2 will be the duplicate number

Time Complexity -> O(n ^ 2) Space Complexity -> O(1)


Using Sorting:
1. Sort the array and find duplicate number by traversing the array.

Time Complexity -> O(nlogn) Space -> O(1)


Using HasMap or HashSet:
1. Get the frequency map of the array
2. The element which has frequency of 2 will be the duplicate number

Time Complexity -> O(n) Space Complexity -> O(n)


Using Linked List Cycle Method:
Approach -> Neetcode

Time Complexity -> O(N) Space -> O(1)
"""

from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]
        return slow
