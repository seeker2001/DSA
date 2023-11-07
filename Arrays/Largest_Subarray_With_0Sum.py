"""
GFG
Problem Statement: Given an array containing both positive and negative integers, 
we have to find the length of the longest subarray with the sum of all elements equal to
zero.

Brute Force Approach:
1. Try out all the possible subarrays.
2. Return the length of the largest subarray whose sum is equal to 0.

Time Complexity -> O(N ^ 2) Space Complexity -> O(1)

Optimal Approach:
1. Keep track of sum upto the current index (i).
2. If you have not seen the sum before
    (a) Store the sum in the hashmap mapping it to the current index (i)
   Otherwise
    (a) If we have we have seen the current sum before (index j) this means that the
        elements after the index j upto i have sum equal to 0 i.e. we have found subarray
        with sum 0.
    (b) Take max of this subarray length with result.
3. Return the result

Time Complexity -> O(N) Space Complexity -> O(N)
"""


class Solution:
    def maxLen(self, n, arr):
        res = 0
        mp = {0: -1}
        csum = 0
        for i in range(n):
            csum += arr[i]
            if csum in mp:
                res = max(res, i - mp[csum])
            else:
                mp[csum] = i
        return res
