# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}" if self.next else str(self.val)


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ret = n = None
        n1, n2 = list1, list2
        while n1 and n2:
            if n1.val <= n2.val:
                next_n = ListNode(n1.val)
                n1 = n1.next
            else:
                next_n = ListNode(n2.val)
                n2 = n2.next
            if not ret:
                ret = n = next_n
            else:
                n.next = next_n
                n = next_n

        for n12 in [n1, n2]:
            if n12:
                if not ret:
                    ret = n12
                else:
                    n.next = n12
        return ret


s = Solution()

for l1, l2 in [
    (ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))),
    (None, None),
    (None, ListNode(0)),
]:
    print("---------------", l1, l2, s.mergeTwoLists(l1, l2), sep="\n")
