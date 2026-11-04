# 25. Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Example 1:

#  1 -> 2 -> 3 -> 4 -> 5
#  2 -> 1 -> 4 -> 3 -> 5

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:

#  1 -> 2 -> 3 -> 4 -> 5
#  3 -> 2 -> 1 -> 4 -> 5

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}" if self.next else str(self.val)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        ret = None
        i = 1
        n = head
        while n:
            rev_n = ListNode(n.val)
            if i % k == 1:
                e = rev_n
            else:
                rev_n.next = prev
                if i % k == 0:
                    e.next = n.next
                    if not ret:
                        ret = rev_n
                    else:
                        prev_e.next = rev_n
                    prev_e = e
            prev = rev_n
            i += 1
            n = n.next
        return ret if ret else head


#  1 -> 2 -> 3 -> 4 -> 5
#  1                      n = 1 e = 1
#  2 -> 1 -> 3 ...        n = 2 e = 1 prev_e = 1
#  2 -> 1    3            n = 3 e = 3 prev_e = 1
#  2 -> 1 -> 4 -> 3 -> 5  n = 4 e = 3 prev_e = 1


s = Solution()

for head, k in [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3),
]:
    print(
        "---------------",
        f"list: {head}",
        f"k: {k}",
        s.reverseKGroup(head, k),
        sep="\n",
    )
