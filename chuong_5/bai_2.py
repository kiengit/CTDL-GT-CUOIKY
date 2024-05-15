class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def ChieuCao(self, node):
        if node is None:
            return 0
        else:
            left_height = self.ChieuCao(node.left)
            right_height = self.ChieuCao(node.right)
            return max(left_height, right_height) + 1

# Ví dụ sử dụng
# Tạo các nút
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Tạo cây nhị phân
binary_tree = BinaryTree(root)

# In chiều cao của cây
print("Chiều cao của cây:", binary_tree.ChieuCao(root))
