# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:


# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        n1, n2 = head, head.next
        ret = head.next
        while n1 and n2:
            n3 = n2.next
            n4 = n3.next if n3 else None
            n1.next, n2.next = n4 if n4 else n3, n1
            n1, n2 = n3, n4
        return ret


def nodes_to_list(n: ListNode | None):
    l = []
    while n:
        l.append(n.val)
        n = n.next
    return l


s = Solution()
print(nodes_to_list(s.swapPairs(None)))
print(nodes_to_list(s.swapPairs(ListNode(1))))
print(nodes_to_list(s.swapPairs(ListNode(1, ListNode(2, ListNode(3))))))
print(nodes_to_list(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))))
