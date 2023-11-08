"""
Leetcode : 3
Problem Statement: Given a String, find the length of longest substring without any 
repeating character.

Brute Force Approach:
1. Try all the substrings without any repeating character (use a set to check for this).
2. Return the length of the longest one.

Time Complexity -> O(N^2) Space Complexity -> O(N)

Optimal Approach (SLiding Window):
1. Use two pointers left and right, where right pointer will be used to traverse the string
and left pointer will point to the start of the window.
2. We will use a set to store the character of the window. If the current character is
already in window we start moving the left pointer to get rid of duplicate and removing 
the characters as you go in the set.
3. Finally whatever be the largest size of set will be, that will be the longest substring
without repeating characters.

Time Complexity -> O(N) Space Complexity -> O(N) 
"""
from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, len(charSet))
        return res
