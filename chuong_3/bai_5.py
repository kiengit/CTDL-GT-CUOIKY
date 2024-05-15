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

    def Tich(self, dathuc2):
        # Tạo một đa thức mới để lưu kết quả tích
        result = dathuc()

        # Duyệt qua từng số hạng trong dathuc1
        current1 = self.Head
        while current1 is not None:
            # Duyệt qua từng số hạng trong dathuc2
            current2 = dathuc2.Head
            while current2 is not None:
                # Nhân hai số hạng và thêm vào đa thức kết quả
                heso = current1.HeSo * current2.HeSo
                somu = current1.SoMu + current2.SoMu
                result.Them(heso, somu)
                current2 = current2.KeTiep
            current1 = current1.KeTiep

        # Rút gọn đa thức kết quả và trả về
        result.RutGon()
        return result

    def inDanhSach(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep

# Tạo hai đa thức
dathuc1 = dathuc()
dathuc1.Them(3, 2)
dathuc1.Them(-5, 1)
dathuc1.Them(2, 0)

dathuc2 = dathuc()
dathuc2.Them(4, 3)
dathuc2.Them(2, 1)
dathuc2.Them(1, 0)

print("Đa thức 1:")
dathuc1.inDanhSach()
print("\nĐa thức 2:")
dathuc2.inDanhSach()

# Tính tích của hai đa thức và in kết quả
result = dathuc1.Tich(dathuc2)
print("\nĐa thức tích:")
result.inDanhSach()
