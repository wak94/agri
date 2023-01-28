"""
@file: LeetCode1664.py
@author: wak
@date: 2023/1/28 9:35 
"""
from collections import Counter
from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans = s = 0
        # 计算偶数下标元素和与奇数下标元素和的差值
        sign = 1
        # 计算到下标i为止的偶数下标元素和减去奇数下标元素和的差值
        cnt = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            s += nums[i] * sign
            cnt[i] = s
            sign = -sign
        if s == nums[0]:
            ans += 1
        for i in range(1, len(nums)):
            if cnt[i - 1] == s - cnt[i]:
                ans += 1
        return ans
