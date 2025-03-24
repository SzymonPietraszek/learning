NUM_OF_CHARS_PER_VALUE = 2

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.parent: Node = None
		self.left: Node = left
		self.right: Node = right
		if left:
			left.parent = self
		if right:
			right.parent = self

	def __str__(self) -> str:
		return str(self.value).rjust(NUM_OF_CHARS_PER_VALUE, " ") if self\
				else '.' * NUM_OF_CHARS_PER_VALUE
