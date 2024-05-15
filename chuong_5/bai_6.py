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
        return max(self.ChieuCao(node.left), self.ChieuCao(node.right)) + 1

    def KiemTraBST(self, node, min_value=float("-inf"), max_value=float("inf")):
        if node is None:
            return True
        
        if not (min_value <= node.data <= max_value):
            return False
        
        return (self.KiemTraBST(node.left, min_value, node.data - 1) and 
                self.KiemTraBST(node.right, node.data + 1, max_value))
    
    def KiemTraAVL(self, node):
        if node is None:
            return True
        
        # Kiểm tra chiều cao của cây con bên trái và bên phải
        left_height = self.ChieuCao(node.left)
        right_height = self.ChieuCao(node.right)
        if abs(left_height - right_height) > 1:
            return False
        
        # Kiểm tra cây con bên trái và bên phải
        if not self.KiemTraAVL(node.left) or not self.KiemTraAVL(node.right):
            return False
        
        # Kiểm tra xem cây có phải là cây BST không
        return self.KiemTraBST(node)

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

# Kiểm tra xem cây có phải là cây AVL không
if binary_tree.KiemTraAVL(root):
    print("Cây là cây AVL.")
else:
    print("Cây không phải là cây AVL.")
