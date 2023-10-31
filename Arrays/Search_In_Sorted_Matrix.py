"""
Leetcode : 74
Problem Statement: You have been given a 2-D array ‘mat’ of size ‘N x M’ where ‘N’ and 
‘M’ denote the number of rows and columns, respectively. The elements of each row are 
sorted in non-decreasing order. Moreover, the first element of a row is greater than the
last element of the previous row (if it exists). You are given an integer ‘target’, and 
your task is to find if it exists in the given ‘mat’ or not.

Brute Force Approach:
1. Simply search the target value by going through the entire matrix

Time Complexity -> O(M * N) Space Complexity -> O(1)

Better Approach:
1. Go through all the rows in the matrix and by comparing target value to first and last
value of the row, see where the target value can lie in.
2. Now simply do a binary search for target value in the row.

Time Complexity -> O(M + logN) Space Complexity -> O(1)

Optimal Approach:
1. See the matrix like a simple linear array and apply binary search.
2. for a value mid, row = mid // N and col = mid % N

Time Complexity -> O(log(M*N)) Space Complexity -> O(1)
"""

from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        lo, hi = 0, M * N - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            row, col = mid // N, mid % N
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
