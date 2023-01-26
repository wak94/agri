"""
@file: LeetCode1662.py
@author: wak
@date: 2023/1/26 15:52 
"""
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        s2 = ""
        for i in range(len(word1)):
            s1 += word1[i]
        for i in range(len(word2)):
            s2 += word2[i]
        return s1 == s2
        # 以上代码可以用下面一行代码代替
        # return ''.join(word1) == ''.join(word2)


print(Solution().arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
print(Solution().arrayStringsAreEqual(["a", "bc"], ["ab", "c"]))
