"""
Leetcode : 62
Problem Statement: Given a matrix m X n, count paths from left-top to the right bottom 
of a matrix with the constraints that from each cell you can either only move to the 
rightward direction or the downward direction.

Brute Force Approach:
1. The Problem can be solved using recursion. We just need to calculate the total no of 
ways to reach bottom right cell from top left cell
2. The number of ways to react bottom right cell from a cell (i, j) will be:
    ways(i, j) = ways(i + 1, j) + ways(i, j + 1)

Time Complexity -> O(2^(M * N)) Space Complexity -> O(M + N)

Optimal Approach:
1. We can use memoization or tabulation (faster) to optimize the solution because of 
repeatition of subproblems
2. for tabulation -> dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

Time Complexity -> O(M * N) Space Complexity -> O(M * N)

Space Optimized Solution:
1. To find the answers for a row we just need the current and next row. So, we should be
storing those only.

Time Complexity -> O(M * N) Space Complexity -> O(N)


Maths Solutions:
Combinatorics Solution:
1. No of ways :  C(m + n - 2, m - 1) or C(m+n-2, m-1)

Time Complexity -> O(m - 1) or O(n - 1) Space Complexity -> O(1)
"""
from typing import *


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            nxt = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    nxt[j] = 1
                else:
                    nxt[j] = nxt[j + 1] + cur[j]
            cur = nxt
        return cur[0]


# Maths Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = n + m - 2
        r = m - 1
        res = 1
        for i in range(1, r + 1):
            res = res * (N - r + i) / i
        return int(res)
