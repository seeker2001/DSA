"""
Coding Ninja
Problem Statement: Given an array of integers A and an integer B. Find the total number 
of subarrays having bitwise XOR of all elements equal to k.

Brute Force Approach:
1. Try all the subarrays and find their xor value.
2. If the xor value of subarray is K increment result by 1
3. Return the result

Time Complexity -> O(N^2) Space Complexity -> O(1)

Optimal Approach (Using Hashmap):
Key Points: (1) We know a^a = 0 and a^0 = a. We will be taking advantage of these properties of xor 
operator here

1. Calculate the xor of the elements in the array as you traverse it. Let the xor upto index i
is curXor.
2. We want to know how many subarrays ending at i have xor value equal to K. If there is/are
subarrays with xor value k ending at i then we can write: 
    before ^ k = curXor (where before will be the xor of the elements left to next)
    before = curXor ^ k.
3. So at each index we want to know how many such "before" values exist and that will be
the count of subarrays with value k ending at i.
4. Store curXor in hashmap with its count (freq) as its value.
5. Do this for the entire array and return the result.
 
Time Complexity -> O(N) Space Complexity -> O(N)
"""
from typing import *


def subarraysWithSumK(a: [int], b: int) -> int:
    # Write your code here
    mp = {0: 1}
    curXor = 0
    res = 0
    for n in a:
        curXor ^= n
        res += mp.get(curXor ^ b, 0)
        mp[curXor] = mp.get(curXor, 0) + 1
    return res
