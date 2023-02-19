# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 50000 
#  0 <= nums[i] <= 10000 
#  
# 
#  Related Topics 数组 双指针 排序 👍 279 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            # 前奇后偶
            if nums[i] & 1 and not nums[j] & 1:
                i += 1
                j -= 1
            # 前偶后奇
            elif not nums[i] & 1 and nums[j] & 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            # 都是奇数
            elif nums[i] & 1:
                i += 1
            else:
                j -= 1
        return nums
# leetcode submit region end(Prohibit modification and deletion)
