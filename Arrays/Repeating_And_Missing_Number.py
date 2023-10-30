"""
Coding Ninja

Problem Statement: You are given a read-only array of N integers with values also in the
range [1, N] both inclusive. Each integer appears exactly once except A which appears 
twice and B which is missing. The task is to find the repeating and missing numbers A 
and B where A repeats twice and B is missing.


Burte Force Approach:
1. Use two nested loop where in the outer loop we will pick element from 1 to N, and in 
inner loop find its count in the array.
2. Element with count -> 0 (missing number) and Element with count -> 2 (repeating number)

Time Complexity -> O(N ^ 2) Space Complexity -> O(1)

Using HashMap or Frequency Array (Better Approach):
1. Find frequency of number from 1 to N and then find the missing and repeating number

Time Complexity -> O(N) Space Complexity -> O(N)


Using Maths (Optimal Approach 1):
1. For two numbers A and B we will find two equations using the sum of first N natural 
number and product of N natural number.
2. Solve the equations to find A and B
[Integer Overflow issues]

Time Complexity -> O(N) Space Complexity -> O(1)

Using Xor Operator (Optimal Approach 2):
1. In first step we will find A ^ B by taking xor of the array and numbers from 1 to N
2. Then we will find rsb (rightmost set bit mask) from A ^ B
3. We will divide the numbers 1 to N and of the array to two sets where this bit is set
and where its not.
4. We will take xor of these values as we divide the numbers into these categories. After
we are done one of the number will be A and other will be B
5. Iterate over the array to find which is the missing and repeating number among two. 

Time Complexity -> O(N) Space Complexity -> O(1) 
"""

from typing import *


def missingAndRepeating(arr, N):
    xor = 0
    for i in range(N):
        xor ^= arr[i]
        xor ^= i + 1

    rsb = xor & -xor
    setBit, notSetBit = 0, 0
    for i in range(N):
        if arr[i] & rsb:
            setBit ^= arr[i]
        else:
            notSetBit ^= arr[i]
        if rsb & (i + 1):
            setBit ^= i + 1
        else:
            notSetBit ^= i + 1
    for num in arr:
        if num == setBit:
            return notSetBit, setBit
        elif num == notSetBit:
            return setBit, notSetBit
