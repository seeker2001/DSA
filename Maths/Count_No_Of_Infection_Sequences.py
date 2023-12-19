"""
You are given an integer n and a 0-indexed integer array sick which is sorted in increasing order.

There are n children standing in a queue with positions 0 to n - 1 assigned to them. The array sick contains
the positions of the children who are infected with an infectious disease. An infected child at position i 
can spread the disease to either of its immediate neighboring children at positions i - 1 and i + 1 if they 
exist and are currently not infected. At most one child who was previously not infected can get infected 
with the disease in one second.

It can be shown that after a finite number of seconds, all the children in the queue will get infected with
the disease. An infection sequence is the sequential order of positions in which all of the non-infected
children get infected with the disease. Return the total number of possible infection sequences.

Since the answer may be large, return it modulo 109 + 7.

Note that an infection sequence does not contain positions of children who were already infected with the
disease in the beginning.


Solution: (Using Combinatorics)
1. Suppose if the sequence of children is  XOOOX (X - infected, O - healthy). Then, the number of ways the 
children could become infected will be  2 * 2 * 2 * 1 i.e. in general if there are m children between infected
children then the number of seq. will be 2 ^(m - 1)

2. Now we can also have case like XOOOXOOX. In this case 4 and 3 children between the infected can become 
infected in (2 ^ 3 and 2 ^ 2) ways. So, for the give entire sequence the number of ways will be 8 * 4 = 32.
But 32 is simply the number of combination while we are looking for the number of sequences (permutations)
so we need to multiply this with (3 + 4)! / 3! * 4! (for including the permutations for each comb.)

--> Look in solution for explaination of each step.

Time Complexity -> O(n * logn) Space Complexity -> O(n)

"""
from typing import *
from functools import cache


class Solution:
    MOD = 10**9 + 7

    @staticmethod
    @cache
    def factorial(x: int):
        if x == 0:
            return 1
        return x * Solution.factorial(x - 1) % Solution.MOD

    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        """
        Here we are including length of starting ending sequences of uninfected children for e.g. if you have
        OOXOOOXOOXOOO then length of starting and ending seq. 2 and 3 will be added to the lengths array
        """
        lengths = [sick[0], n - sick[-1] - 1]

        # include the length of seq. of children between infected children
        for i in range(1, len(sick)):
            cur, prev = sick[i], sick[i - 1]
            length = cur - prev - 1
            if length > 0:
                lengths.append(length)

        res = Solution.factorial(sum(lengths))
        for i, l in enumerate(lengths):
            res *= pow(Solution.factorial(l), -1, Solution.MOD)
            res %= Solution.MOD

            # for starting and ending seq there is only one combination
            if i >= 2:
                res *= pow(2, l - 1, Solution.MOD)
                res %= Solution.MOD
        return res
