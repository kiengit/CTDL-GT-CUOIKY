class HanoiTower:
    def __init__(self, so_tang):
        self.so_tang = so_tang

    def di_chuyen(self, n, vi_tri_a, vi_tri_c, vi_tri_b):
        if n == 1:
            print("Di chuyển tầng 1 từ", vi_tri_a, "đến", vi_tri_c)
            return
        self.di_chuyen(n-1, vi_tri_a, vi_tri_b, vi_tri_c)
        print("Di chuyển tầng", n, "từ", vi_tri_a, "đến", vi_tri_c)
        self.di_chuyen(n-1, vi_tri_b, vi_tri_c, vi_tri_a)

# Ví dụ sử dụng
so_tang = 3
thap = HanoiTower(so_tang)
thap.di_chuyen(so_tang, 'A', 'C', 'B')
