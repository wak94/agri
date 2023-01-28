"""
@file: LeetCode2541.py
@author: wak
@date: 2023/1/28 15:00 
"""
import collections
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = s = 0
        for x, y in zip(nums1, nums2):
            x = x - y
            # k为0时必须全为0
            if k:
                # 首先k必须是flag[i]的因子
                if x % k:
                    return -1
                s += x
                if x > 0:
                    ans += x // k
            # 若k为0，只要x不为0就返回-1
            elif x:
                return -1
        # 如果差值的和不为0返回-1
        return -1 if s else ans

    def firstUniqChar(self, s: str) -> str:
        cnt = collections.Counter(s)
        for x in s:
            if cnt[x] == 1:
                return x
        return ' '


print(Solution().firstUniqChar('cc'))
