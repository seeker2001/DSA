"""
Coding Ninja
Problem Statement: Given an array of N integers, count the inversion of the array.
What is an inversion of an array? Definition: for all i & j < size of array, if i < j 
then you have to find pair (A[i],A[j]) such that A[j] < A[i].


Brute Force Approach:
1. Try all possible pair of values using two nested loops.
2. Count the total inversions and return the value

Time Complexity -> O(N ^ 2) Space Complexity -> O(1)

Optimal Approach:
1. Use Merge Sort to find the count of inversions.
2. We will be counting the inversions when the subarrays are merged.

Time Complexity -> O(NlogN) Space Complexity -> O(1)
"""


def merge(left, right, arr, res):
    nl, nr = len(left), len(right)
    i, j, k = 0, 0, 0
    while i < nl and j < nr:
        if left[i] > right[j]:
            arr[k] = right[j]
            res[0] = res[0] + nl - i
            j += 1
        else:
            arr[k] = left[i]
            i += 1
        k += 1
    while i < nl:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < nr:
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


def mergeSort(arr, res):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left, right = mergeSort(arr[:mid], res), mergeSort(arr[mid:], res)
    return merge(left, right, arr, res)


def getInversions(arr, n):
    res = [0]
    mergeSort(arr, res)
    return res[0]
