NUM_OF_CHARS_PER_VALUE = 2


class Node:
    def __init__(self, value: int, parent=None):
        self.value: int = value
        self.parent: Node = parent
        self.left: Node = None
        self.right: Node = None

    def __str__(self) -> str:
        return str(self.value).rjust(NUM_OF_CHARS_PER_VALUE, " ") if self\
               else '.' * NUM_OF_CHARS_PER_VALUE


class BST:
    def __init__(self):
        self.root: Node = None

    def _find(self, value: int) -> tuple[Node, Node]:
        parent = None
        node = self.root

        while node and node.value != value:
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right

        return (parent, node)

    def insert(self, value: int) -> Node:
        if not self.root:
            self.root = Node(value)
            return

        parent, node = self._find(value)
        if node:  # there is already a node with value
            return node

        new_node = Node(value, parent)
        if new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        return new_node

    def search(self, value: int) -> Node:
        _, node = self._find(value)
        return node

    def delete(self, value: int) -> Node:
        found = self.search(value)
        if not found:
            return None

        if found.left and found.right:  # if there are two children
            nextInOrderNode = found.right
            while nextInOrderNode.left:
                nextInOrderNode = nextInOrderNode.left

            # swap found value with the next in order
            found.value = nextInOrderNode.value
            # mark the next in order node to be deleted
            found = nextInOrderNode

        # found node has at maximum one non nil child
        child = found.left if found.left else found.right
        if child:
            child.parent = found.parent

        parent = found.parent
        if not parent:
            self.root = child
            return self.root

        if parent.left == found:
            parent.left = child
        else:
            parent.right = child
        return parent

    def print(self):
        layers = [[self.root]]
        values = []
        sep = [0, NUM_OF_CHARS_PER_VALUE]

        while not all(n is None for n in layers[-1]):
            values.append([str(n.value) if n else "." * NUM_OF_CHARS_PER_VALUE
                           for n in layers[-1]])
            layers.append([m for n in layers[-1] for m in
                           ([n.left, n.right] if n else [None, None])])
            sep.append(sep[-1]*NUM_OF_CHARS_PER_VALUE + NUM_OF_CHARS_PER_VALUE)

        for i, values in enumerate(values):
            print(" "*sep[-3 - i], sep="", end="")
            print((" "*sep[-2 - i]).join(values))
