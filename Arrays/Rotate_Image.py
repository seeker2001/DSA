"""
Leetcode : 48
Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

Brute Force Solution:
1. Initialize a dummy matrix of the same size as the given matrix.
2. Now copy the the columns the original matrix left to right (iterating through elements 
down to top) and copy them into the dummy matrix row wise top to bottom.
2. Finally copy the content of dummy matrix into the original matrix

Time complexity => O(N * N) Space complexity -> O(N * N)

Optimized Solution **:
1. Take the transpose of the matrix
2. Reverse the rows of the matrix

Time complexity -> O(N * N) Space complexity -> O(1)

Optimized Solution 2:
Neetcode

Time complexity -> O(N * N) Space complexity -> O(1)
"""


# Optimized Solution 1
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        # take transpose of the matrix
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse the rows
        for i in range(N):
            l, r = 0, N - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1


# Optimized Solution 2
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        L, R = 0, N - 1
        while L < R:
            T, B = L, R
            for i in range(R - L):
                topLeft = matrix[T][L + i]
                matrix[T][L + i] = matrix[B - i][L]
                matrix[B - i][L] = matrix[B][R - i]
                matrix[B][R - i] = matrix[T + i][R]
                matrix[T + i][R] = topLeft
            L += 1
            R -= 1
