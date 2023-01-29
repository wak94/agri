"""
@file: LeetCode2527.py
@author: wak
@date: 2023/1/29 19:48 
"""
from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans
