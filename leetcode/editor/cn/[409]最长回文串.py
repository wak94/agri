# 给定一个包含大写字母和小写字母的字符串
#  s ，返回 通过这些字母构造成的 最长的回文串 。 
# 
#  在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入:s = "abccccdd"
# 输出:7
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#  
# 
#  示例 2: 
# 
#  
# 输入:s = "a"
# 输出:1
#  
# 
#  示例 3： 
# 
#  
# 输入:s = "aaaaaccc"
# 输出:7 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 2000 
#  s 只由小写 和/或 大写英文字母组成 
#  
# 
#  Related Topics 贪心 哈希表 字符串 👍 500 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        cnt = collections.Counter(s)
        for val in cnt.values():
            ans += val // 2 * 2
            if ans % 2 == 0 and val %2 == 1:
                ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
