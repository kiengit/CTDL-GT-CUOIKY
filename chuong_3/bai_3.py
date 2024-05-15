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

    def Cong(self, other):
        # Tạo một đa thức mới để lưu kết quả
        result = dathuc()
        
        # Duyệt qua các số hạng trong hai đa thức
        current1 = self.Head
        current2 = other.Head
        while current1 is not None and current2 is not None:
            # Nếu số mũ của số hạng trong đa thức 1 nhỏ hơn số mũ của số hạng trong đa thức 2
            if current1.SoMu < current2.SoMu:
                result.Them(current1.HeSo, current1.SoMu)
                current1 = current1.KeTiep
            # Nếu số mũ của số hạng trong đa thức 1 lớn hơn số mũ của số hạng trong đa thức 2
            elif current1.SoMu > current2.SoMu:
                result.Them(current2.HeSo, current2.SoMu)
                current2 = current2.KeTiep
            # Nếu số mũ của số hạng trong đa thức 1 bằng số mũ của số hạng trong đa thức 2
            else:
                # Cộng hệ số của hai số hạng có cùng số mũ và thêm vào đa thức kết quả
                result.Them(current1.HeSo + current2.HeSo, current1.SoMu)
                current1 = current1.KeTiep
                current2 = current2.KeTiep

        # Thêm các số hạng còn lại của đa thức 1 vào đa thức kết quả
        while current1 is not None:
            result.Them(current1.HeSo, current1.SoMu)
            current1 = current1.KeTiep

        # Thêm các số hạng còn lại của đa thức 2 vào đa thức kết quả
        while current2 is not None:
            result.Them(current2.HeSo, current2.SoMu)
            current2 = current2.KeTiep

        # Rút gọn đa thức kết quả và trả về
        result.RutGon()
        return result

    def inDanhSach(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep

# Tạo một đa thức thứ nhất
dathuc1 = dathuc()
dathuc1.Them(3, 2)
dathuc1.Them(-5, 1)
dathuc1.Them(2, 0)
dathuc1.Them(4, 3)

# Tạo một đa thức thứ hai
dathuc2 = dathuc()
dathuc2.Them(2, 2)
dathuc2.Them(3, 1)
dathuc2.Them(1, 0)
dathuc2.Them(-4, 3)

# Tính tổng của hai đa thức và in kết quả
print("Đa thức tổng:")
result = dathuc1.Cong(dathuc2)
result.inDanhSach()
