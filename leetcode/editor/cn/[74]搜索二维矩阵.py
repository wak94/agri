# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -10⁴ <= matrix[i][j], target <= 10⁴ 
#  
# 
#  Related Topics 数组 二分查找 矩阵 👍 766 👎 0
from bisect import bisect_left
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, x in enumerate(matrix):
            h = x[0]
            t = x[-1]
            if h <= target <= t:
                index = bisect_left(matrix[i], target)
                if index < len(matrix[0]) and matrix[i][index] == target:
                    return True
                else:
                    return False
        return False
# leetcode submit region end(Prohibit modification and deletion)
