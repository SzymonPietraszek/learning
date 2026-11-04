# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        ret = None
        prev = None
        rest = 0
        while l1 or l2 or rest:
            s = rest + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            n = ListNode(s % 10)
            if prev:
                prev.next = n
                prev = n
            else:
                ret = prev = n
            rest = s // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return ret


s = Solution()
print(
    s.addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))
    )
)
print(s.addTwoNumbers(ListNode(0), ListNode(0)))
print(
    s.addTwoNumbers(
        ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
            ),
        ),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
    )
)
