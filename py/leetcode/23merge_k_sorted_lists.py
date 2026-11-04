# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

from heapq import heappush, heappop
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}" if self.next else str(self.val)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = None
        h = []
        d = defaultdict(list)
        for l in lists:
            if l:
                heappush(h, l.val)
                d[l.val].append(l)
        while h:
            m = heappop(h)
            ml = d[m].pop()
            if ml.next:
                heappush(h, ml.next.val)
                d[ml.next.val].append(ml.next)

            n = ListNode(m)

            if not ret:
                ret = n
            else:
                prev.next = n
            prev = n
        return ret


s = Solution()

for ls in [
    [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ],
    [],
    [[]],
]:
    print("---------------", *ls, s.mergeKLists(ls), sep="\n")
