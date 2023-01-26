"""
@file: LeetCode1748.py
@author: wak
@date: 2023/1/26 16:06 
"""
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        # [] 为列表 List
        # {} 为字典 也就是键值对类型的数据结构，类似于Java中的f
        f = {}
        for i in nums:
            if i not in f:
                ans += i
                f[i] = 1
            elif f[i] == 1:
                ans -= i
                f[i] = 2
        return ans


print(Solution().sumOfUnique([1, 2, 3, 2]))
