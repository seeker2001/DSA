"""
Leetcode : 2953
You are given a string word and an integer k.
A substring s of word is complete if:
    1. Each character in s occurs exactly k times.
    2. The difference between two adjacent characters is at most 2. That is, for any two adjacent characters
    c1 and c2 in s, the absolute difference in their positions in the alphabet is at most 2.
Return the number of complete substrings of word.


Solution -> Sliding Window Approach
1. Divide string into parts where condition 2 is met. Find answer for all parts individually and sum of 
these will be the answer for complete string.
2. For each part -> The max number of unique characters in string can be 26. Therefore the substrings that
we are looking for will have length as 1 * k, 2 * k , .........., 26 * k in general i * k where k is given 
to us and i will be the number of unique characters.
3. Now we will consider substring with 1 unique character to substring with 26 unique characters. To find 
the desired substring we will use sliding window technqiue
(look in code of ref)

Time Complexity -> O(n * 26 * 26)  Space Complexity -> O(n)

"""


class Solution:
    # function checks if the sub has i unique chars with k freq each
    def checkValidSub(self, mp, i, k):
        count = 0
        for key in mp:
            if mp[key] == 0:
                continue
            if mp[key] != k:
                return False
            count += 1
        if count != i:
            return False
        return True

    # function finds number of substrings where count of each character is k
    def countSubstrings(self, s, k):
        count = 0
        # i -> number of unique characters
        for i in range(1, 27):
            subLength = i * k
            # if subLength exceeds length of s, we will stop
            if subLength > len(s):
                break
            mp = {}
            # using sliding window consider all subs of length subLength
            for j in range(len(s)):
                if j < subLength:
                    mp[s[j]] = mp.get(s[j], 0) + 1
                else:
                    if self.checkValidSub(mp, i, k):
                        count += 1
                    mp[s[j]] = mp.get(s[j], 0) + 1
                    mp[s[j - subLength]] -= 1
            if self.checkValidSub(mp, i, k):
                count += 1
        return count

    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        res, cur = 0, ""
        for i in range(n):
            # considering parts individually
            if i > 0 and abs(ord(word[i]) - ord(word[i - 1])) > 2:
                res += self.countSubstrings(cur, k)
                cur = ""
            cur += word[i]
        res += self.countSubstrings(cur, k)
        return res
