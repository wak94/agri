"""
@file: LeetCode6365.py
@author: wak
@date: 2023/2/20 15:00 
"""


class Solution:
    def minOperations(self, n: int) -> int:
        def dfs(k: int) -> int:
            if k & (k - 1) == 0:
                return 1
            lb = k & -k
            return 1 + min(dfs(lb + k), dfs(k - lb))

        return dfs(n)


nums = [5, 7, 7, 8, 8, 10]
i, j = 0, len(nums) - 1
target = 8
while i <= j:
    mid = (i + j) // 2
    if nums[mid] > target:
        j = mid - 1
    else:
        i = mid + 1
print(i)
