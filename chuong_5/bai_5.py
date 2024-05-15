class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def KiemTraBST(self, node, min_value=float("-inf"), max_value=float("inf")):
        if node is None:
            return True
        
        # Kiểm tra giá trị của nút
        if not (min_value <= node.data <= max_value):
            return False
        
        # Kiểm tra cây con bên trái và cây con bên phải của nút hiện tại
        return (self.KiemTraBST(node.left, min_value, node.data - 1) and 
                self.KiemTraBST(node.right, node.data + 1, max_value))

# Ví dụ sử dụng
# Tạo các nút
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(7)

# Tạo cây nhị phân
binary_tree = BinaryTree(root)

# Kiểm tra xem cây có phải là cây BST không
if binary_tree.KiemTraBST(root):
    print("Cây là cây BST.")
else:
    print("Cây không phải là cây BST.")
