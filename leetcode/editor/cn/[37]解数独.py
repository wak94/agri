# 编写一个程序，通过填充空格来解决数独问题。 
# 
#  数独的解法需 遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图） 
#  
# 
#  数独部分空格内已填入了数字，空白格用 '.' 表示。 
# 
#  
# 
#  
#  
#  
#  示例 1： 
#  
#  
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".
# ",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".
# ","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6
# "],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[
# ".",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8
# "],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],[
# "4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9",
# "6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4",
# "5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
#  
#  
#  
#  
# 
# 
# 
#  
# 
#  提示： 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] 是一位数字或者 '.' 
#  题目数据 保证 输入数独仅有一个解 
#  
# 
#  Related Topics 数组 哈希表 回溯 矩阵 👍 1525 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.dfs(board)

    def dfs(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.check(board, i, j, k):
                            board[i][j] = str(k)
                            if self.dfs(board):
                                return True
                            board[i][j] = '.'
                    # 无法填入数字
                    return False
        return True

    # 判断第i行第j列填入value是否合理
    def check(self, board: List[List[str]], row: int, col: int, value: int) -> bool:
        # 判断该行
        for i in range(9):
            if board[row][i] == str(value):
                return False
        # 判断列
        for j in range(9):
            if board[j][col] == str(value):
                return False
        # 判断九宫格
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(value):
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
