"""
Leetcode: 73
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to
set its entire column and row to 0 and then return the matrix.

Brute Force Solution: 
1. Define a new matrix (temp) of the same size as given and copy the element into this 
new matrix
2. Traverse through the original matrix and if you find a 0 then set the entire row and
column of the element to 0 in the temp
3. Finally copy the content of new matrix in the original matrix

Time Complexity -> O(M*N(M+N)) Space Complexity -> O(M*N)

Better Approach:
1. Traverse the matrix and store the row and column indexes of elements which are 0 in
two sets (for row and columns)
2. Then go through these columns and rows and set the elements in them to 0
 
Time Complexity -> O(M * N) Space Complexity -> O(M + N)

Optimal Approach:
1. Use the first row and column to store the information about the rows and columns to
be made equal to 0.
2. When you find a 0 in the matrix set the first element in its row and column to 0
3. Now traverse the matrix and looking at the first element in the row and column of that
element set it to 0.

Imp. point -> In this approach we will be using the first element of matrix at (0, 0) for
storing the info about both first row and column.So to avoid this we will instead use a
separate variable for one of them.

Time Complexity -> O(M * N) Space Complexity -> O(1)
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        row0 = False
        # step 1 & 2
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    if r == 0:
                        row0 = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0

        # step 3
        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Handle the first row and column
        if matrix[0][0] == 0:
            for r in range(M):
                matrix[r][0] = 0
        if row0:
            for c in range(N):
                matrix[0][c] = 0
