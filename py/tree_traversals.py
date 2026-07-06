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
    s = []
    while s or n:
        if n:
            ret.append(n.val)
            s.append(n.right)
            n = n.left
        else:
            n = s.pop()

    return ret


# left right root
def traverse_postorder(n: Node):
    ret = []
    s = []
    prev = None
    while s or n:
        if n:
            s.append(n)
            n = n.left
            continue
        p = s[-1]
        if p.right and p.right != prev:
            n = p.right
            continue
        n = s.pop()
        ret.append(n.val)
        prev = n
        n = None
    return ret


def bfs(n: Node):
    ret = []
    q = [n]
    while q:
        n = q[0]
        q = q[1:]
        if n:
            ret.append(n.val)
            q.append(n.left)
            q.append(n.right)
    return ret


bst = Node(4, Node(2, Node(1), Node(3)), Node(5, None, Node(6)))

print("tree:")
print("     4")
print("   /   \\")
print("  2     5")
print(" / \\     \\")
print("1   3     6")
print("DFS inorder  ", traverse_inorder(bst))
print("DFS preorder ", traverse_preorder(bst))
print("DFS postorder", traverse_postorder(bst))
print("BFS          ", bfs(bst))
