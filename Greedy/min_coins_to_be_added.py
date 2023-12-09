"""
Leetcode : 2952

You are given a 0-indexed integer array coins, representing the values of the coins available, 
and an integer target. An integer x is obtainable if there exists a subsequence of coins that sums to x.
Return the minimum number of coins of any value that need to be added to the array so that every integer 
in the range [1, target] is obtainable.


Solution:
Greedy Approach:
1. Sort the coins array
2. Now we will need a variable to keep track of max value upto which the values are achievable currently
(current_max [initially = 0])
3. Now we will run a loop until current_max >= target 
    (a) if cur_coin <= current_max + 1 -> this means that we can obtain values from [1, current_max + cur_coin]
    (b) else this will mean that we cannot get the value current_max + 1, and many more depending on the
        cur_coin value  so add a coin of value current_max + 1 which will change our current_max to 
        current_max += (current_max + 1)
        
        e.g. [1, 2, ......., current_max] -> already achievable 
        now if cur_coin > current_max + 1 (let cur_coin = current_max + 2) 
        i will have values [1, 2, ....., current_max, current_max + 2, current_max + 3, ...]
        current_max + 1 -> missing (so we need to add the coin of this value)
4. return number of coins added

Time complexity -> O(nlogn)  Space complexity -> O(1)
"""
from typing import *


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        coins_added = 0
        current_max = 0
        index = 0
        while current_max < target:
            if index < len(coins) and coins[index] <= current_max + 1:
                current_max += coins[index]
                index += 1
            else:
                current_max += current_max + 1
                coins_added += 1
        return coins_added
