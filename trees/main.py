from bst import BST
from avl import AVL

if __name__ != "__main__":
    quit()

# change tree type
#  -----------------
tree = BST()
# tree = AVL()
# -----------------


print("Empty tree print")
tree.print()
print(f"Empty tree search {tree.search(0)}")
tree.delete(0)
print("Empty tree delete")

for i in [60, 40, 30, 70, 80, 50, 10, 20]:
    print(f"insert({i})")
    tree.insert(i)
    tree.print()

for i in [30, 60, 50, 90]:
    print(f"search({i}): {tree.search(i)}")

for i in [30, 50, 70, 60]:
    print(f"delete({i})")
    tree.delete(i)
    tree.print()
