"""
Leetcode: 118 (Variation 3)

Problem Statement: This problem has 3 variations. They are stated below:

Variation 1: Given row number r and column number c. Print the element at position (r, c) in
Pascal's triangle.
Variation 2: Given the row number n. Print the n-th row of Pascal's triangle.
Variation 3: Given the number of rows n. Print the first n rows of Pascal's triangle.

Variation 1: 
C(r - 1, c - 1)
Time Complexity -> O(r) Space Complexity -> O(1)

Variation 2: 
Current element = prevElement * (rowNumber - colIndex) / colIndex
Time Complexity -> O(N) Space Complexity -> O(1)

Variation 3:
Time Complexity -> O(N^2) Space Complexity -> O(1)

Algorithm:
https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/

"""


# Variation 1
def nCr(n, r):
    ans = 1
    for i in range(r):
        ans *= n - i
        ans //= i + 1
    return ans


def pascalTriangle(r, c):
    # the element at position (r, c) ->  C(r - 1, c - 1)
    return nCr(r - 1, c - 1)


# Variation 2
def pascalTriangle(r):
    row = [1]
    for i in range(1, r):
        cur = row[i - 1] * (r - 1)
        cur //= i
        row.append(cur)
    return row


# Variation 3
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for r in range(2, numRows + 1):
            cur = [1] * (r)
            for i in range(1, r - 1):
                cur[i] = res[-1][i - 1] + res[-1][i]
            res.append(cur)
        return res
