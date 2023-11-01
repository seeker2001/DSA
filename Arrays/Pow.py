"""
Leetcode : 50
Problem Statement: Given a double x and integer n, calculate x raised to power n. 
Basically Implement pow(x, n).

Brute Force Approach:
1. Store the absolute value of n in some variable (nn)
2. Now calculate pow(x, nn) by simply running a loop n times and in each iteration multiply
ans with x (initialize ans = 1)
3. Finally if x was negative divide the 1 by ans and return

Time Complexiity -> O(n) Space Complexity -> O(1)

Binary Exponentiation (Optimal Approach):
1. Store the absolute value of n in some variable (nn)
2. Now in each step divide nn by half there will be 2 cases:
    (a) if n is odd -> then ans = x * (pow(x, n // 2)) ^ 2
    (b) if n is even -> then ans = (pow(x, n// 2)) ^ 2
3. Finally if x was negative divide the 1 by ans and return

Time Complexity -> O(logn) Space Complexity -> O(1)
"""

from typing import *


class Solution:
    def findPow(self, x, n):
        if n == 0:
            return 1
        subRes = self.findPow(x, n // 2)
        if n % 2:
            return x * subRes * subRes
        return subRes * subRes

    def myPow(self, x: float, n: int) -> float:
        nn = abs(n)
        ans = self.findPow(x, nn)
        return ans if n >= 0 else 1 / ans
