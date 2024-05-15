class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def SoSanhNode(self, node1, node2):
        # Nếu cả hai nút đều là None, chúng giống nhau
        if node1 is None and node2 is None:
            return True
        # Nếu chỉ một trong hai nút là None, chúng không giống nhau
        if node1 is None or node2 is None:
            return False
        # So sánh giá trị của hai nút và tiếp tục so sánh các nút con của chúng
        return (node1.data == node2.data and
                self.SoSanhNode(node1.left, node2.left) and
                self.SoSanhNode(node1.right, node2.right))

    def SoSanh(self, other_tree):
        return self.SoSanhNode(self.root, other_tree.root)

# Ví dụ sử dụng
# Tạo cây nhị phân thứ nhất
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# Tạo cây nhị phân thứ hai giống hệt cây thứ nhất
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

# Tạo cây nhị phân thứ ba khác với cây thứ nhất
root3 = Node(1)
root3.left = Node(3)
root3.right = Node(2)

binary_tree1 = BinaryTree(root1)
binary_tree2 = BinaryTree(root2)
binary_tree3 = BinaryTree(root3)

# So sánh cây nhị phân thứ nhất với cây nhị phân thứ hai
print("Cây 1 giống cây 2:", binary_tree1.SoSanh(binary_tree2))  # Kết quả True

# So sánh cây nhị phân thứ nhất với cây nhị phân thứ ba
print("Cây 1 giống cây 3:", binary_tree1.SoSanh(binary_tree3))  # Kết quả False
