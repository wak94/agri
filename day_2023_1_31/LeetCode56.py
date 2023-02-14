"""
@file: LeetCode56.py
@author: wak
@date: 2023/1/31 9:24 
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        n = len(intervals)
        ans = []
        for interval in intervals:
            s = interval[0]
            e = interval[1]
            if s > end:
                ans.append([start, end])
                start = s
                end = e
            if s <= end <= e:
                end = e
        ans.append([start, end])
        return ans
