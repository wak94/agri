"""
@file: 2023_3_5.py
@author: wak
@date: 2023/3/5 19:01 
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def search_BST(self, root: TreeNode, key: int) -> TreeNode:
        if not root or key == root.val:
            return root
        elif key < root.val:
            return self.search_BST(root.left, key)
        else:
            return self.search_BST(root.right, key)

    def insert_BST(self, root: TreeNode, key: int) -> None:
        if not root:
            root = TreeNode(key)
        elif key < root.val:
            self.insert_BST(root.left, key)
        elif key > root.val:
            self.insert_BST(root.right, key)

    def create_BST(self, root: TreeNode) -> None:
        root = None
        e = int(input())
        while e != -1:
            self.insert_BST(root, e)
            e = int(input())
