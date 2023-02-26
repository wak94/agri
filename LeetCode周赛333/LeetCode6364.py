"""
@file: LeetCode6364.py
@author: wak
@date: 2023/2/20 15:17 
"""
from typing import List

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
mask = [0] * 31

for i in range(2, 31):
    for j, x in enumerate(primes):
        if i % x == 0:
            if i % (x * x) == 0:
                mask[i] = -1
                break
            mask[i] |= 1 << j  # 把第j个质数加到集合


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:


print(Solution().squareFreeSubsets([3, 4, 4, 5]))
