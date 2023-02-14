"""
@file: LeetCode77.py
@author: wak
@date: 2023/2/6 10:01 
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(n, k, t):
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(t, n + 1):
                path.append(i)
                dfs(n, k, i + 1)
                path.pop()

        dfs(n, k, 1)
        return ans


print(Solution().combine(4, 2))
