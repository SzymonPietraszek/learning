from enum import Enum
from node import Node


class Order(Enum):
	PREORDER_ = 1
	INORDER__ = 2
	POSTORDER = 3

def depth_first_search(root: Node, ord: Order):
	if ord in [Order.PREORDER_, Order.INORDER__, Order.POSTORDER]:
		print(f"depth first search {ord}: {collect_DFS(root, ord)}")

def collect_DFS(node: Node, ord: Order) -> list[int]:
	if not node:
		return []

	left, root, right = collect_DFS(node.left, ord), [node.value], collect_DFS(node.right, ord)
	match ord:
		case Order.PREORDER_:
			return root + left + right
		case Order.INORDER__:
			return left + root + right
		case Order.POSTORDER:
			return left + right + root

def breadth_first_search(root: Node):
	values = collect_BFS(root) if root else []
	print(f"breadth first search              : {values}")

def collect_BFS(root: Node) -> list[int]:
	values = []
	nodes = [root]
	while nodes:
		n = nodes.pop(0)
		values.append(n.value)
		if n.left:
			nodes.append(n.left)
		if n.right:
			nodes.append(n.right)
	return values

def test_tree_traversal():
	root = Node(4,
		Node(2,
			Node(1),
			Node(3)),
		Node(5,
			None,
			Node(6)))

	print("tree:")
	print("     4")
	print("   /   \\")
	print("  2     5")
	print(" / \\     \\")
	print("1   3     6")

	depth_first_search(root, Order.PREORDER_)
	depth_first_search(root, Order.INORDER__)
	depth_first_search(root, Order.POSTORDER)
	breadth_first_search(root)