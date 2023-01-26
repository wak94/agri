"""
@file: LeetCode2544.py
@author: wak
@date: 2023/1/26 22:14 
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        flag = True
        s = str(n)
        for i in range(len(s)):
            if flag:
                ans += int(s[i])
                flag = False
            else:
                ans -= int(s[i])
                flag = True
        return ans

    def alternateDigitSum1(self, n: int) -> int:
        ans, flag = 0, 1
        while n:
            ans += n % 10 * flag
            flag *= -1
            n //= 10
        return ans * -flag


print(Solution().alternateDigitSum(886996))
