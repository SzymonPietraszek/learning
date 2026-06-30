from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# left root rigth
def traverse_inorder(n: Node):
    ret = []
    s = []
    while s or n:
        if n:
            s.append(n)
            n = n.left
            continue
        n = s.pop()
        ret.append(n.val)
        n = n.right
    return ret


# root left right
def traverse_preorder(n: Node):
    ret = []
    q = deque([n])
    while q:
        n = q.popleft()
        ret.append(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return ret


# left right root
def traverse_postorder(n: Node):
    ret = []
    s = []
    visited = []
    while True:
        if n.left and n.left not in visited:
            s.append(n)
            n = n.left
            continue
        if n.right and n.right not in visited:
            s.append(n)
            n = n.right
            continue

        ret.append(n.val)
        visited.append(n)
        if s:
            n = s.pop()
        else:
            break
    return ret


def traverse_postorder_smart(n: Node):
    ret = []
    s = []
    v = None
    while s or n:
        if n:
            s.append(n)
            n = n.left
            continue
        t = s[-1]
        if t.right and not v == t.right:
            n = t.right
            continue
        n = s.pop()
        ret.append(n.val)
        v = n
        n = None
    return ret


bst = Node(4, Node(2, Node(1), Node(3)), Node(5, None, Node(6)))

print("tree:")
print("     4")
print("   /   \\")
print("  2     5")
print(" / \\     \\")
print("1   3     6")
print("traverse inorder  ", traverse_inorder(bst))
print("traverse preorder ", traverse_preorder(bst))
print("traverse postorder", traverse_postorder(bst))
print("postorder smarter ", traverse_postorder_smart(bst))
