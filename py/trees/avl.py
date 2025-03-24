from bst import BST, Node


class AVL(BST):
    def __init__(self):
        super().__init__()
        self.heights = {None: 0}

    def insert(self, value: int):
        p = super().insert(value)
        self.fix_heights(p)

        c, cc = None, None
        while p:
            if self.is_unbalanced(p):
                self.balance(p, c, cc)
                break
            p, c, cc = p.parent, p, c

    def delete(self, val: int):
        p = super().delete(val)
        self.fix_heights(p)

        while p:
            if self.is_unbalanced(p):
                c = self.get_child_with_max_height(p, False)
                cc = self.get_child_with_max_height(c, c == p.left)
                self.balance(p, c, cc)
            p = p.parent

    def get_child_with_max_height(self, n: Node, if_equal_left: bool):
        hl, hr = self.heights[n.left], self.heights[n.right]
        if hl > hr or (hl == hr and if_equal_left):
            return n.left
        return n.right

    def fix_heights(self, n: Node):
        while n:
            self.heights[n] = 1 + max(
                self.heights[n.left],
                self.heights[n.right])
            n = n.parent

    def is_unbalanced(self, n: Node) -> bool:
        return abs(self.heights[n.left] - self.heights[n.right]) > 1

    def balance(self, p: Node, c: Node, cc: Node):
        if (p.left == c) != (c.left == cc):
            # left, right or right, left rotations
            self.rotate(c, cc)
            c = cc  # after rotation a child of child of parent becomes
            # a child of parent (goes up)
        self.rotate(p, c)

    def rotate(self, p: Node, c: Node):
        right = p.left == c
        print("rotate", p.value, c.value, "right:", str(right).lower())

        t0, t2 = p.parent, c.right if right else c.left
        p.parent, c.parent = c, t0
        if right:
            p.left, c.right = t2, p
        else:
            p.right, c.left = t2, p

        if t2:
            t2.parent = p

        if not t0:
            self.root = c
        elif t0.left == p:
            t0.left = c
        elif t0.right == p:
            t0.right = c

        self.fix_heights(p)

#      y                               x
#     / \     Right Rotation          /  \
#    x   T3   - - - - - - - >        T1   y
#   / \       < - - - - - - -            / \
#  T1  T2     Left Rotation            T2  T3


# rotate right
#      t0         t0
#      |          |
#      p          c
#     / \    =>  /  \
#    c   t3     t1   p
#   / \             / \
#  t1  t2         t2  t3
# rotate left
#    t0              t0
#    |               |
#    p               c
#   /  \     =>     / \
#  t1   c          p   t3
#      / \        / \
#    t2  t3      t1  t2
