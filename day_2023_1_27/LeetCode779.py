"""
@file: LeetCode779.py
@author: wak
@date: 2023/1/27 13:43 
"""
from typing import List


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (k & 1) ^ 1 ^ self.kthGrammar(n - 1, (k + 1) // 2)


print(Solution().kthGrammar(2, 2))
a = 1
b = 0
c1 = (a & 1) ^ 1 ^ b
c2 = ~((a & 1) ^ b)
print(c1 == c2)
