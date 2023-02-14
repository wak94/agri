"""
@file: LeetCode24.py
@author: wak
@date: 2023/2/1 13:38 
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(0)
        h.next = head
        tmp = h
        # 当后两个节点都不为空就交换，之后跳跃两个节点
        while tmp.next and tmp.next.next:
            newNode = tmp.next
            tmp.next = tmp.next.next
            newNode.next = tmp.next.next
            tmp.next.next = newNode
            tmp = tmp.next.next
        return h.next
