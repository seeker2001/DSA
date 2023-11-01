"""
Leetcode : 169
Problem Statement: Given an array of N integers, write a program to return an element 
that occurs more than N/2 times in the given array. You may consider that such an element
always exists in the array.

Brute Force Approach:
1. Using 2 nested loops, pick an element in the outer loop and count its frequency in the
inner loop
2. return the element which is present more than half times

Time Complexity -> O(N ^ 2) Space Complexity -> O(1)

Using Hashing (Better Approach):
1. Use a hashmap to find frequency of the element and return the element present more than
half times.

Time Complexity -> O(N) Space Complexity -> O(N)

Moore's Voting ALgo (Optimal Apporach):
1. This approach is based on the logic of cancellation i.e each occurence of the majority
element can be mapped to othe elements in the array and still at the end we will be left
with at least one occurence of the majority element

Time Complexity -> O(N) Space Complexity -> O(1) 
"""

from typing import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, freq = -1, 0
        for n in nums:
            if freq == 0:
                ans = n
            if ans == n:
                freq += 1
            else:
                freq -= 1
        return ans
