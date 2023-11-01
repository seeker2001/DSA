"""
Leetcode : 229
Problem Statement: Given an array of N integers. Find the elements that appear more than
N/3 times in the array. If no such element exists, return an empty vector.

Prerequisite -> Majority_Element

Optimal Approach (Modified Moore's Voting Algo):
1. This approach can be applied in a general case of N/K.
2. Use a counter to implement this solution.
3. Traverse the array and keep on adding the elements into the counter till the size of 
counter becomes K - 1 and store their frequency as well
4. If you see an element which is already present in the counter increase its frequency
otherwise decrease the frequency of all the elements inside by 1 (logic of cancellation).
5. Finally whatever elements are present in counter are the majority elements (potential, 
check their frequency to verify).

Time Complexity -> O(N) Space Complexity -> O(1)
"""
from typing import *

from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = Counter()
        for n in nums:
            if n in ctr or len(ctr) < 2:
                ctr[n] += 1
            else:
                ctr -= Counter(set(ctr.keys()))
        return [n for n in ctr.keys() if nums.count(n) > len(nums) // 3]
