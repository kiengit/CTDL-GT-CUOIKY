class BieuThuc:
    def __init__(self, bieu_thuc):
        self.bieu_thuc = bieu_thuc

    def HauTo(self):
        # Hàm ưu tiên của các toán tử
        def uu_tien(op):
            if op == '+' or op == '-':
                return 1
            elif op == '*' or op == '/':
                return 2
            return 0

        toan_hang = []
        toan_tu = []
        hau_to = []

        i = 0
        while i < len(self.bieu_thuc):
            if self.bieu_thuc[i].isdigit():
                so = ''
                while i < len(self.bieu_thuc) and (self.bieu_thuc[i].isdigit() or self.bieu_thuc[i] == '.'):
                    so += self.bieu_thuc[i]
                    i += 1
                hau_to.append(so)
            elif self.bieu_thuc[i] == '(':
                toan_tu.append(self.bieu_thuc[i])
                i += 1
            elif self.bieu_thuc[i] == ')':
                while toan_tu[-1] != '(':
                    hau_to.append(toan_tu.pop())
                toan_tu.pop()
                i += 1
            else:
                while toan_tu and uu_tien(self.bieu_thuc[i]) <= uu_tien(toan_tu[-1]):
                    hau_to.append(toan_tu.pop())
                toan_tu.append(self.bieu_thuc[i])
                i += 1

        while toan_tu:
            hau_to.append(toan_tu.pop())

        return ' '.join(hau_to)

# Ví dụ
bieu_thuc = "2 + 3 * 5"
bt = BieuThuc(bieu_thuc)
print("Biểu thức hậu tố:", bt.HauTo())  # Kết quả: '2 3 5 * +'
