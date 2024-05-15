class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def SoNutLa(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.SoNutLa(node.left) + self.SoNutLa(node.right)

# Ví dụ sử dụng
# Tạo các nút
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Tạo cây nhị phân
binary_tree = BinaryTree(root)

# In số nút lá của cây
print("Số nút lá của cây:", binary_tree.SoNutLa(root))
