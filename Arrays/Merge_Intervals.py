"""
Leetcode : 56
Problem Statement: Given an array of intervals, merge all the overlapping intervals and
return an array of non-overlapping intervals.

Optimal Approach:
1. Sort the intervals array based on the start value.
2. Traverse the intervals array [current Interval(start, end) & prevEnd: end value of 
last added interval in the answer list]
    -> if start > prevEnd : then add the interval to answer list
    -> else: merge the current interval into last added interval in answer list
     
Time Complexity -> O(N * LogN) Space Complexity -> O(N) [for answer list] 
"""
import math


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        prevEnd = -math.inf
        for start, end in intervals:
            if start > prevEnd:
                ans.append([start, end])
            else:
                ans[-1][1] = max(ans[-1][1], end)
            prevEnd = max(prevEnd, end)
        return ans
