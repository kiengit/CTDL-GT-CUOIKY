class BieuThuc:
    def __init__(self, bieu_thuc):
        self.bieu_thuc = bieu_thuc

    def GiaTri(self):
        # Hàm ưu tiên của các toán tử
        def uu_tien(op):
            if op == '+' or op == '-':
                return 1
            elif op == '*' or op == '/':
                return 2
            return 0

        # Hàm thực hiện phép toán
        def tinh(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                return a / b

        toan_hang = []
        toan_tu = []

        i = 0
        while i < len(self.bieu_thuc):
            if self.bieu_thuc[i].isdigit():
                so = 0
                while i < len(self.bieu_thuc) and self.bieu_thuc[i].isdigit():
                    so = so * 10 + int(self.bieu_thuc[i])
                    i += 1
                toan_hang.append(so)
            elif self.bieu_thuc[i] == '(':
                toan_tu.append(self.bieu_thuc[i])
                i += 1
            elif self.bieu_thuc[i] == ')':
                while toan_tu[-1] != '(':
                    b = toan_hang.pop()
                    a = toan_hang.pop()
                    op = toan_tu.pop()
                    toan_hang.append(tinh(a, b, op))
                toan_tu.pop()
                i += 1
            else:
                while toan_tu and uu_tien(self.bieu_thuc[i]) <= uu_tien(toan_tu[-1]):
                    b = toan_hang.pop()
                    a = toan_hang.pop()
                    op = toan_tu.pop()
                    toan_hang.append(tinh(a, b, op))
                toan_tu.append(self.bieu_thuc[i])
                i += 1

        while toan_tu:
            b = toan_hang.pop()
            a = toan_hang.pop()
            op = toan_tu.pop()
            toan_hang.append(tinh(a, b, op))

        return toan_hang[-1]

# Ví dụ
bieu_thuc = "3 + 4 * 2 / (1 - 5)"
bt = BieuThuc(bieu_thuc)
print("Giá trị của biểu thức là:", bt.GiaTri())  # Kết quả: -5
