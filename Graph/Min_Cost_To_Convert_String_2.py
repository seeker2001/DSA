"""
Leetcode : 2977
Problem Statement : You are given two 0-indexed strings source and target, both of length n and consisting 
of lowercase English characters. You are also given two 0-indexed string arrays original and changed, and 
an integer array cost, where cost[i] represents the cost of converting the string original[i] to the string
changed[i].

You start with the string source. In one operation, you can pick a substring x from the string, and change 
it to y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and 
changed[j] == y. You are allowed to do any number of operations, but any pair of operations must satisfy 
either of these two conditions:

The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In 
other words, the indices picked in both operations are disjoint.
The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other 
words, the indices picked in both operations are identical.
Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Solution: (Approach - 1) (TLE)
1. First we will find out the min cost to transform one string to other using the original, changed and cost
array (using Floyd Warshall algo)
2. Then we can use recursion (with memoization) to find the actual min cost to change source to target acc 
to the problem.

Approach-2:
1. Here we use Dijkstra algo, we find out single pair shortest path and cache the results from this for future
use.
2. Some optimization here to avoid TLE

"""
from typing import *
from math import inf
from collections import defaultdict
from functools import cache
import heapq


## Results in TLE
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # we create an adjacency list from the original, changed and cost array --> dist
        dist = defaultdict(lambda: defaultdict(lambda: inf))
        orig_to_new = [(original[i], changed[i], cost[i]) for i in range(len(cost))]
        orig_to_new.sort(key=lambda x: (x[0], x[1], -x[2]))
        sub = set()
        for i in range(len(cost)):
            dist[orig_to_new[i][0]][orig_to_new[i][1]] = orig_to_new[i][2]
            sub.add(original[i])
            sub.add(changed[i])

        # Use Floyd Warshall Algo to find All pair shortest path
        for s1 in sub:
            for s2 in sub:
                for s3 in sub:
                    dist[s2][s3] = min(dist[s2][s3], dist[s2][s1] + dist[s1][s3])

        # Simply use recursion along with memoization to find minCost
        @cache
        def dfs(i):
            if i == len(source):
                return 0

            minCost = inf
            if source[i] == target[i]:
                minCost = min(minCost, dfs(i + 1))

            for j in range(i, len(source)):
                sub_source = source[i : j + 1]
                sub_target = target[i : j + 1]
                if dist[sub_source][sub_target] != inf:
                    minCost = min(minCost, dist[sub_source][sub_target] + dfs(j + 1))

            return minCost

        res = dfs(0)
        return res if res != inf else -1


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # get the adjL from original, changed and cost array
        adj = defaultdict(lambda: defaultdict(int))
        for i, start in enumerate(original):
            end = changed[i]
            c = cost[i]

            if end in adj[start]:
                adj[start][end] = min(adj[start][end], c)
            else:
                adj[start][end] = c

        # This array will help us in optimization when calculating min cost to change source to target
        change_lengths = set(len(sub) for sub in original)

        # Dijkstra algo to find shortest path (min cost) from start to end (caching used)
        @cache
        def dijkstra(start, end):
            heap = [(0, start)]
            costs = defaultdict(lambda: inf)
            costs[start] = 0
            while heap:
                path_cost, curr = heapq.heappop(heap)
                if curr == end:
                    return path_cost
                for nei in adj[curr]:
                    nei_cost = adj[curr][nei]

                    new_cost = nei_cost + path_cost

                    if new_cost < costs[nei]:
                        costs[nei] = new_cost
                        heapq.heappush(heap, (new_cost, nei))
            return inf

        @cache
        def dfs(i):
            # let dfs(i) be the cost of matching everything at i and onwards assuming everything before i
            # is matched
            if i >= len(target):
                return 0
            # if they match save default cost as just continue
            c = inf if target[i] != source[i] else dfs(i + 1)
            # we consider only those length substring after i that we can transform
            for length in change_lengths:
                t_sub = target[i : i + length]
                s_sub = source[i : i + length]
                trans_cost = dijkstra(s_sub, t_sub)

                if trans_cost != inf:
                    c = min(c, trans_cost + dfs(i + length))
            return c

        ans = dfs(0)

        return ans if ans != inf else -1
