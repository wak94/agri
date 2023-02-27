# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入:a = "11", b = "1"
# 输出："100" 
# 
#  示例 2： 
# 
#  
# 输入：a = "1010", b = "1011"
# 输出："10101" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a.length, b.length <= 10⁴ 
#  a 和 b 仅由字符 '0' 或 '1' 组成 
#  字符串如果不是 "0" ，就不含前导零 
#  
# 
#  Related Topics 位运算 数学 字符串 模拟 👍 968 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        c = 0
        ans = []
        while i >= 0 and j >= 0:
            x = int(a[i])
            y = int(b[j])
            ans.insert(0, str((x + y + c) % 2))
            c = (x + y + c) // 2
            i -= 1
            j -= 1
        while i >= 0:
            x = int(a[i])
            ans.insert(0, str((x + c) % 2))
            c = (x + c) // 2
            i -= 1
        while j >= 0:
            y = int(b[j])
            ans.insert(0, str((y + c) % 2))
            c = (y + c) // 2
            j -= 1
        if c == 1:
            ans.insert(0, '1')
        return ''.join(ans)
# leetcode submit region end(Prohibit modification and deletion)
