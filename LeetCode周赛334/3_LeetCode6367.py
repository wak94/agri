"""
@file: 3_LeetCode6367.py
@author: wak
@date: 2023/2/26 11:08 
"""
from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) // 2 + 1
        while left + 1 < right:
            k = (left + right) // 2
            if all(nums[i] * 2 <= nums[i - k] for i in range(k)):
                left = k
            else:
                right = k

        return left * 2
