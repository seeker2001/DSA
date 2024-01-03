"""
There is a company with n branches across the country, some of which are connected by roads. Initially, all
branches are reachable from each other by traveling some roads.
The company has realized that they are spending an excessive amount of time traveling between their branches.
As a result, they have decided to close down some of these branches (possibly none). However, they want to 
ensure that the remaining branches have a distance of at most maxDistance from each other.
The distance between two branches is the minimum total traveled length needed to reach one branch from 
another.
You are given integers n, maxDistance, and a 0-indexed 2D array roads, where roads[i] = [ui, vi, wi] 
represents the undirected road between branches ui and vi with length wi.

Return the number of possible sets of closing branches, so that any branch has a distance of at most 
maxDistance from any other.

Note that, after closing a branch, the company will no longer have access to any roads connected to it.

Note that, multiple roads are allowed.

Solution:
1. Try all possible subsets and using floyd warshall algo see if the set is a valid set.

Time Complexity -> O(2 ^ n * n ^ 3)  Space Complexity -> O(n ^ 2)
"""
from copy import deepcopy
from typing import *
import math


class Solution:
    def getMaxDist(self, mask, n, minDist):
        res = 0
        for k in range(n):
            if mask & (1 << k):
                for i in range(n):
                    if i != k and (mask & (1 << i)):
                        for j in range(n):
                            if j != i and (mask & (1 << j)):
                                minDist[i][j] = min(
                                    minDist[i][j], minDist[i][k] + minDist[k][j]
                                )
        # find maxDist outside the loop where you are finding minDist for every pair of nodes
        for i in range(n):
            if mask & (1 << i):
                for j in range(i + 1, n):
                    if mask & (1 << j):
                        res = max(res, minDist[i][j])
        return res

    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        minDist = [[math.inf] * n for i in range(n)]
        for i, j, d in roads:
            minDist[i][j] = min(minDist[i][j], d)
            minDist[j][i] = min(minDist[j][i], d)
        comb = 1 << n
        res = 1
        for mask in range(1, comb):
            # the minDist array should not be changed after calling the function for next iteration
            # therefore we will create a deepcopy of the same
            res += self.getMaxDist(mask, n, deepcopy(minDist)) <= maxDistance
        return res
