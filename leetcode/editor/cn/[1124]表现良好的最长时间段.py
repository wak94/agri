# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。 
# 
#  我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。 
# 
#  所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。 
# 
#  请你返回「表现良好时间段」的最大长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。 
# 
#  示例 2： 
# 
#  
# 输入：hours = [6,6,6]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hours.length <= 10⁴ 
#  0 <= hours[i] <= 16 
#  
# 
#  Related Topics 栈 数组 哈希表 前缀和 单调栈 👍 393 👎 0
from collections import Counter
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        s = [0]
        stk = [0]
        for i in range(len(hours)):
            s.append(s[i] + (1 if hours[i] > 8 else -1))
            if s[stk[-1]] > s[i + 1]:
                stk.append(i + 1)
        ans = 0
        for r in range(len(hours), 0, -1):
            while stk and s[stk[-1]] < s[r]:
                ans = max(ans, r - stk[-1])
                stk.pop()
        return ans

# leetcode submit region end(Prohibit modification and deletion)
