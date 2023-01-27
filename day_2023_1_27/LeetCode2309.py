"""
@file: LeetCode2309.py
@author: wak
@date: 2023/1/27 13:26 
"""
import string


class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for low, up in zip(reversed(string.ascii_lowercase), reversed(string.ascii_uppercase)):
            if low in s and up in s:
                return up
        return ' '


print(Solution().greatestLetter('lEeTcOdE'))
