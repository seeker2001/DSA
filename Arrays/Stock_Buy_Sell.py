"""
Leetcode: 121
Problem Statement: You are given an array of prices where prices[i] is the price of a given
stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock. Return the maximum profit you can achieve 
from this transaction. If you cannot achieve any profit, return 0.


Brute Force Solution:
1. Try every possible combination for buy and sell and return whichever yields max profit.

Time Complexity -> O(n^2) Space -> O(1)

Optimized Solution:
READ:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems

1. The maximum profit we can earn by selling on day i will be when we buy the stock at min
price from (0 to i - 1)
2. Find the max value of this profit for i from 0 to n - 1

Time Complexity -> O(n) Space -> O(1)

"""

import math


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        T_ik0, T_ik1 = 0, -math.inf
        for p in prices:
            T_ik0 = max(T_ik0, p + T_ik1)
            T_ik1 = max(T_ik1, -p)
        return T_ik0
