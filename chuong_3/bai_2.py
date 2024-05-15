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

    def RutGon(self):
        # Duyệt qua các số hạng trong đa thức
        current = self.Head
        while current is not None:
            # Tìm số hạng có cùng số mũ với số hạng hiện tại
            temp = current.KeTiep
            while temp is not None:
                if temp.SoMu == current.SoMu:
                    # Cộng hệ số của hai số hạng có cùng số mũ
                    current.HeSo += temp.HeSo
                    # Loại bỏ số hạng temp
                    current.KeTiep = temp.KeTiep
                temp = temp.KeTiep
            # Di chuyển đến số hạng tiếp theo trong đa thức
            current = current.KeTiep

        # Loại bỏ các số hạng có hệ số bằng 0
        prev = None
        current = self.Head
        while current is not None:
            if current.HeSo == 0:
                if prev is None:
                    self.Head = current.KeTiep
                else:
                    prev.KeTiep = current.KeTiep
            else:
                prev = current
            current = current.KeTiep

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
p.Them(4, 2)

# Rút gọn đa thức
print("Đa thức sau khi rút gọn:")
p.RutGon()
p.inDanhSach()
