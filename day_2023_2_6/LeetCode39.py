"""
@file: LeetCode39.py
@author: wak
@date: 2023/2/6 12:37 
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(candidates, target, s, index):
            # 达到target就添加到答案
            if s == target:
                ans.append(path[:])
                return
            # 遍历到下标为index时，从该下标开始遍历candidates
            for i in range(index, len(candidates)):
                # 如果加上当前下标的这个数已经大于target就没必要继续，直接退出循环
                if candidates[i] + s > target:
                    break
                x = candidates[i]
                path.append(x)
                s += x
                dfs(candidates, target, s, i)
                s -= x
                path.pop()

        dfs(candidates, target, 0, 0)
        return ans
