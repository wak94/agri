"""
@file: LeetCode1669.py
@author: wak
@date: 2023/1/30 9:39 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1 = list1
        l2 = list2
        while l2.next:
            l2 = l2.next
        for _ in range(a - 1):
            l1 = l1.next
        left = l1
        for _ in range(b - a + 2):
            l1 = l1.next
        right = l1
        left.next = list2
        l2.next = right
        return list1
