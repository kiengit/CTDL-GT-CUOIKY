class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def KiemTraCayCon(self, node1, node2):
        # Nếu node2 là None, tức là cây con đã được tìm thấy
        if node2 is None:
            return True
        # Nếu node1 là None, tức là cây con không tồn tại trong cây lớn
        if node1 is None:
            return False
        # Kiểm tra xem node2 có là một phần của cây con của node1 không
        return (node1.data == node2.data and
                self.KiemTraCayCon(node1.left, node2.left) and
                self.KiemTraCayCon(node1.right, node2.right))

    def CayCon(self, other_tree):
        return self.KiemTraCayCon(self.root, other_tree.root)

# Ví dụ sử dụng
# Tạo cây nhị phân thứ nhất
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

# Tạo cây nhị phân thứ hai là một phần của cây nhị phân thứ nhất
root2 = Node(2)
root2.left = Node(4)
root2.right = Node(5)

# Tạo cây nhị phân thứ ba không là một phần của cây nhị phân thứ nhất
root3 = Node(4)
root3.left = Node(3)

binary_tree1 = BinaryTree(root1)
binary_tree2 = BinaryTree(root2)
binary_tree3 = BinaryTree(root3)

# Kiểm tra xem cây nhị phân thứ hai có phải là cây con của cây nhị phân thứ nhất không
print("Cây 2 là cây con của cây 1:", binary_tree1.CayCon(binary_tree2))  # Kết quả True

# Kiểm tra xem cây nhị phân thứ ba có phải là cây con của cây nhị phân thứ nhất không
print("Cây 3 là cây con của cây 1:", binary_tree1.CayCon(binary_tree3))  # Kết quả False
