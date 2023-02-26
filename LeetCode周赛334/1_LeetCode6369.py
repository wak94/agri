"""
@file: 1_LeetCode6369.py
@author: wak
@date: 2023/2/26 10:30 
"""
from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        s = sum(nums)
        ans[0] = s - nums[0]
        ans[n - 1] = s - nums[n - 1]
        res = 0
        for i in range(1, n - 1):
            res += nums[i - 1]
            ans[i] = abs(s - 2 * res - nums[i])
        return ans


print(Solution().leftRigthDifference([1]))
