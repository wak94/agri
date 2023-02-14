# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 500] 内 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 10⁹ 
#  
# 
#  Related Topics 链表 双指针 👍 889 👎 0
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        pre = None
        n = 0
        while cur:
            n += 1
            pre = cur
            cur = cur.next
        k %= n
        if k == 0:
            return head
        # 先成环，再找合适的位置断开
        pre.next = head
        cur = head
        k = n - k - 1
        while k:
            cur = cur.next
            k -= 1
        head = cur.next
        cur.next = None
        return head
# leetcode submit region end(Prohibit modification and deletion)
