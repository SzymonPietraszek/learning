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
    q = deque([n])
    while q:
        n = q.popleft()
        print(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)


bst = Node(4, Node(2, Node(1), Node(3)), Node(5, None, Node(6)))

print("traverse inorder ", traverse_inorder(bst))
print("traverse preorder", traverse_preorder(bst))
