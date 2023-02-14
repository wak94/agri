# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。 
# 
#  按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下： 
# 
#  
#  "123" 
#  "132" 
#  "213" 
#  "231" 
#  "312" 
#  "321" 
#  
# 
#  给定 n 和 k，返回第 k 个排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3, k = 3
# 输出："213"
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 4, k = 9
# 输出："2314"
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 3, k = 1
# 输出："123"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  1 <= k <= n! 
#  
# 
#  Related Topics 递归 数学 👍 753 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = [i for i in range(1, n + 1)]
        for i in range(1, k):
            ans = self.operate(ans)
        return ''.join(map(str, ans))

    def operate(self, nums: List[int]):
        i = len(nums) - 2
        # 从后向前找第一个破坏降序的元素
        while i >= 0 and nums[i + 1] < nums[i]:
            i -= 1
        if i >= 0:
            # 如果上述i找到了，就从后往前找第一个大于对应数的下标
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
# leetcode submit region end(Prohibit modification and deletion)
