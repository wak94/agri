"""
@file: LeetCode2537.py
@author: wak
@date: 2023/1/27 19:46 
"""
from collections import Counter
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = left = pairs = 0
        cnt = Counter()
        for x in nums:
            pairs += cnt[x]
            cnt[x] += 1
            # left每动一次就有一个满足条件的子数组，所以每次需要加上left+1
            while pairs - (cnt[nums[left]] - 1) >= k:
                cnt[nums[left]] -= 1
                pairs -= cnt[nums[left]]
                left += 1
            if pairs >= k:
                ans += left + 1
        return ans
