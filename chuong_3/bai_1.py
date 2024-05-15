class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class dathuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        # Tạo nút mới chứa số hạng mới
        new_node = Node(heso, somu)
        
        # Nếu danh sách đang trống, thêm nút mới làm đầu danh sách
        if self.Head is None:
            self.Head = new_node
        else:
            # Duyệt danh sách đến phần tử cuối cùng
            current = self.Head
            while current.KeTiep is not None:
                current = current.KeTiep
            # Thêm nút mới vào sau phần tử cuối cùng
            current.KeTiep = new_node

    def inDanhSach(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep

# Tạo một đa thức mới
p = dathuc()

# Thêm các số hạng vào đa thức
p.Them(3, 2)
p.Them(-5, 1)
p.Them(2, 0)

# In ra đa thức hiện tại
print("Đa thức hiện tại:")
p.inDanhSach()
