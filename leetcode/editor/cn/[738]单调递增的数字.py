# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。 
# 
#  给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 10
# 输出: 9
#  
# 
#  示例 2: 
# 
#  
# 输入: n = 1234
# 输出: 1234
#  
# 
#  示例 3: 
# 
#  
# 输入: n = 332
# 输出: 299
#  
# 
#  
# 
#  提示: 
# 
#  
#  0 <= n <= 10⁹ 
#  
# 
#  Related Topics 贪心 数学 👍 334 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        i = 1
        nums = []
        for x in s:
            nums.append(int(x))
        while i < len(nums) and nums[i - 1] <= nums[i]:
            i += 1
        if i < len(nums):
            # 找i开始往左第一个减一依旧不会破坏递增关系的数
            while i > 0 and nums[i - 1] > nums[i]:
                nums[i - 1] -= 1
                i -= 1
            i += 1
            while i < len(nums):
                nums[i] = 9
        ans = 0
        for x in nums:
            ans = ans * 10 + x
        return ans
# leetcode submit region end(Prohibit modification and deletion)
