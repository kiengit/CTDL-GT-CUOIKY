class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def SaoChepNode(self, node):
        if node is None:
            return None
        new_node = Node(node.data)
        new_node.left = self.SaoChepNode(node.left)
        new_node.right = self.SaoChepNode(node.right)
        return new_node
    
    def Chep(self):
        new_root = self.SaoChepNode(self.root)
        return BinaryTree(new_root)

# Ví dụ sử dụng
# Tạo cây nhị phân ban đầu
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Tạo cây nhị phân mới bằng cách sao chép cây nhị phân ban đầu
binary_tree = BinaryTree(root)
copied_tree = binary_tree.Chep()

# Kiểm tra xem cây mới đã được sao chép đúng chưa bằng cách so sánh địa chỉ của nút gốc
print("Cây gốc ban đầu:", id(binary_tree.root))
print("Cây mới đã sao chép:", id(copied_tree.root))
