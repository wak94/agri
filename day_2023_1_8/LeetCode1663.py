"""
@file: LeetCode1663.py
@author: wak
@date: 2023/1/8 20:45 
"""
from string import ascii_lowercase


class Solution:

    def getSmallestString(self, n: int, k: int) -> str:
        s = []
        for i in range(1, n + 1):
            t = max(1, k - (n - i) * 26)
            k -= t
            s.append(ascii_lowercase[t - 1])
        return "".join(s)




solution = Solution()

print(solution.getSmallestString(3, 27))
print(solution.getSmallestString(5, 73))
