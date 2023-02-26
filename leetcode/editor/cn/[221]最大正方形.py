# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [
# ["1","0","1","0","0"],
# ["1","0","1","1","1"],
# ["1","1","1","1","1"],
# ["1","0","0","1","0"]]
# 输出：4
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] 为 '0' 或 '1' 
#  
# 
#  Related Topics 数组 动态规划 矩阵 👍 1378 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = 0
        if not matrix:
            return ans
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                    ans = max(ans, dp[i][j])
        return ans * ans
# leetcode submit region end(Prohibit modification and deletion)
