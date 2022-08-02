# -*- coding: utf-8 -*-
"""
@author: WangJianWei
@time: 2022/8/2 22:05
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = head = ListNode()
        s = 0
        while l1 or l2 or s > 0:
            a = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode((a + s) % 10)
            s = (a + s) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            p = p.next

        return head.next


link1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9,
                                                                                                     next=ListNode(
                                                                                                         val=9,
                                                                                                         next=ListNode(
                                                                                                             val=9)))))))
link2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))

r = Solution().addTwoNumbers(link1, link2)
rr = []
while 1:
    rr.append(r.val)
    if r.next:
        r = r.next
    else:
        break

print(rr)
