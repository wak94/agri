"""
@file: 2_LeetCode6368.py
@author: wak
@date: 2023/2/26 10:48 
"""
from collections import Counter
from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        res = 0
        div = [0] * n
        for i, x in enumerate(word):
            res = (res * 10 + (int(x) % m)) % m
            if res == 0:
                div[i] = 1
        return div


print(Solution().divisibilityArray("1010", 10))
