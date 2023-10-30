"""
Coding Ninja
Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-
decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first
N elements and modify arr2 so that it contains the last M elements. (donot use any extra
space)

Brute Force Approach:
1. Define a dummy array of size (n + m)
2. Now, merge the 2 sorted arrays arr1 and arr2 in this dummy array
3. Finally copy the first n elements of this dummy array in the arr1 and last m elements
in arr2

Time Complexity -> O(n + m) Space Complexity -> O(n + m)


Optimal Approach 1:

Keypoints: 
-> We know that the arr1 after merging will contain first n smaller elements while arr2
will contain the m largest element of the two arrays. So, the largest value of arr1 after
mergin will be smaller or equal to smallest value of the arr2.

Approach:
1. Use 2 pointers left and right in the arr1 and arr2
2. left will point to the end of arr1 and right will point to the start of arr2
3. left pointer will move towards index 0 while right will move towards the index m - 1.
4. compare the element at index left and right
    (a) if arr1[left] > arr2[right] : swap(arr1[left], arr2[right]) and move the pointers
    (b) if arr1[left] <= arr[right] : move the pointers
5. After step 4 arr1 will contain the first n elements and arr2 will contain the last
m elements. Now we will simply sort the two arrays.

Time Complexity -> O(n + m) + O(n * logn) + O(m * logm) Space Complexity -> O(1)

Optimal Approach 2:
Gap Method from shell sort (striver tutorial)

Time Complexity -> O(n + m * log(n + m)) Space -> O(1)
"""
from typing import *


# Optimal approach 1
def mergeTwoSortedArraysWithoutExtraSpace(arr1: List[int], arr2: List[int]) -> int:
    n, m = len(arr1), len(arr2)
    left, right = n - 1, 0
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1.sort()
    arr2.sort()


# Optimal Approach 2

import math


def mergeTwoSortedArraysWithoutExtraSpace(arr1: List[int], arr2: List[int]) -> int:
    n, m = len(arr1), len(arr2)
    length = n + m
    gap = math.ceil(length / 2)
    while gap > 0:
        left, right = 0, gap
        while right < length:
            if right < n:
                if arr1[left] > arr1[right]:
                    i, j = left, right
                    arr1[i], arr1[j] = arr1[j], arr1[i]
            elif left < n:
                i, j = left, right - n
                if arr1[i] > arr2[j]:
                    arr1[i], arr2[j] = arr2[j], arr1[i]
            else:
                i, j = left - n, right - n
                if arr2[i] > arr2[j]:
                    arr2[i], arr2[j] = arr2[j], arr2[i]
            left += 1
            right += 1
        if gap == 1:
            break
        gap = math.ceil(gap / 2)
