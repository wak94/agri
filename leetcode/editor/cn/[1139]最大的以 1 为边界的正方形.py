# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0
# 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,1,0,0]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 100 
#  1 <= grid[0].length <= 100 
#  grid[i][j] 为 0 或 1 
#  
# 
#  Related Topics 数组 动态规划 矩阵 👍 117 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        right = [[0] * m for _ in range(n)]
        down = [[0] * m for _ in range(n)]
        for row in range(n):
            right[row][m - 1] = grid[row][m - 1]
        for col in range(m):
            down[n - 1][col] = grid[n - 1][col]
        for i in range(n):
            for j in range(m - 2, -1, -1):
                if grid[i][j]:
                    right[i][j] = 1 + right[i][j + 1]
                else:
                    right[i][j] = 0
        for i in range(n - 2, -1, -1):
            for j in range(m):
                if grid[i][j]:
                    down[i][j] = 1 + down[i + 1][j]
                else:
                    down[i][j] = 0
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                border = min(right[i][j], down[i][j])
                if border * border <= ans:
                    continue
                while border * border > ans:
                    if right[i + border - 1][j] >= border and down[i][j + border - 1] >= border:
                        ans = max(ans, border * border)
                        break
                    border -= 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
