# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Follow up: Could you do this in one pass?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        ri = len(nodes) - n
        if ri == 0:
            return head.next
        nodes[ri - 1].next = nodes[ri].next
        return head


s = Solution()

print(
    s.removeNthFromEnd(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
    )
)
print(s.removeNthFromEnd(ListNode(1), 1))
print(s.removeNthFromEnd(ListNode(1, ListNode(2)), 1))
