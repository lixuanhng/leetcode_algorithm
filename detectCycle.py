"""

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

链接：https://leetcode-cn.com/problems/linked-list-cycle-ii

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        flag = False
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break
        if not flag:
            return
        else:
            # 当快慢指针相遇时，让其中任一个指针重新指向头节点，然后让它俩以相同速度前进，
            # 再次相遇时所在的节点位置就是环开始的位置。这是为什么呢？
            slow = head
            pos = 0
            while(slow != fast):
                fast = fast.next
                slow = slow.next
                pos += 1
            return slow