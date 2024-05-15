class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def SoNut(self, node):
        if node is None:
            return 0
        else:
            return self.SoNut(node.left) + self.SoNut(node.right) + 1

# Ví dụ sử dụng
# Tạo các nút
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Tạo cây nhị phân
binary_tree = BinaryTree(root)

# In số nút của cây
print("Số nút của cây:", binary_tree.SoNut(root))
