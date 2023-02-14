"""
@file: LeetCode53.py
@author: wak
@date: 2023/2/6 20:16 
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        def L(nums,target):
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        start = L(nums,target)
        if start == n or nums[start] != target:
            return 0
        end = L(nums,target + 1) -1
        return end - start + 1


print(Solution().search([5, 7, 7, 8, 8, 10], 8))
