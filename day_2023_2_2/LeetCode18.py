"""
@file: LeetCode18.py
@author: wak
@date: 2023/2/2 11:34 
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        ans = []
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                tar = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] < tar:
                        left += 1
                    elif nums[left] + nums[right] > tar:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return ans


ans = tmp = []
t = list("the sky is blue")
n = len(t)
for i in range(n):
    if t[i] == ' ' and t[i - 1] != ' ':
        tmp.append(' ')
        print(tmp)
        s = ''.join(tmp)
        print(s)
        ans.append(s)
        tmp = []
    elif t[i] == ' ' and t[i - 1] == ' ':
        continue
    else:
        tmp.append(t[i])

ans.append(''.join(tmp))
print(ans)
