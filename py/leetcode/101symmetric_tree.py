# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


# Follow up: Could you solve it both recursively and iteratively?


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root or (not root.left and not root.right):
            return True
        if not root.left or not root.right:
            return False
        ns = [root.left, root.right]
        while ns:
            new_ns = []
            for i in range(len(ns) // 2):
                ln, rn = ns[2 * i], ns[2 * i + 1]
                if (
                    ln.val != rn.val
                    or (ln.left is None) != (rn.right is None)
                    or (ln.right is None) != (rn.left is None)
                ):
                    return False
                if ln.left and rn.right:
                    new_ns.extend([ln.left, rn.right])
                if ln.right and rn.left:
                    new_ns.extend([ln.right, rn.left])
            ns = new_ns
        return True


s = Solution()

print(
    s.isSymmetric(
        TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        )
    )
)
print(
    s.isSymmetric(
        TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    )
)
