# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。 
# 
#  假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  示例 1: 
#  
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 991 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        # i 为中序遍历中根节点的索引
        # 左树有i个节点，右树有n-i-1个节点
        i = 0
        while i < len(inorder) and inorder[i] != preorder[0]:
            i += 1
        if i:
            root.left = self.buildTree(preorder[1:i + 1], inorder[0:i])
        if len(inorder) - i - 1:
            root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root
# leetcode submit region end(Prohibit modification and deletion)
