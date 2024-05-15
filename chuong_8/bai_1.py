class TuDien:
    def __init__(self):
        self.tudien = {}

    def NhapTu(self, tu, dongnghia=None, trai_ngghia=None):
        # Hàm băm
        hash_key = tu[0]

        # Kiểm tra xem từ đã tồn tại trong từ điển chưa
        if hash_key in self.tudien:
            self.tudien[hash_key][tu] = {'DongNghia': dongnghia, 'TraiNghia': trai_ngghia}
        else:
            self.tudien[hash_key] = {tu: {'DongNghia': dongnghia, 'TraiNghia': trai_ngghia}}

    def TraTu(self, tu):
        hash_key = tu[0]
        if hash_key in self.tudien and tu in self.tudien[hash_key]:
            return self.tudien[hash_key][tu]
        else:
            return {'DongNghia': None, 'TraiNghia': None}

# Ví dụ sử dụng
td = TuDien()
td.NhapTu("mèo", "cat", "chó")
td.NhapTu("chó", "dog", "mèo")
td.NhapTu("vàng", "yellow", "xanh")

tu_can_tra = "mèo"
ket_qua_tra = td.TraTu(tu_can_tra)
print(f"Từ đồng nghĩa của '{tu_can_tra}': {ket_qua_tra['DongNghia']}")
print(f"Từ trái nghĩa của '{tu_can_tra}': {ket_qua_tra['TraiNghia']}")

tu_can_tra = "chó"
ket_qua_tra = td.TraTu(tu_can_tra)
print(f"Từ đồng nghĩa của '{tu_can_tra}': {ket_qua_tra['DongNghia']}")
print(f"Từ trái nghĩa của '{tu_can_tra}': {ket_qua_tra['TraiNghia']}")

tu_can_tra = "vàng"
ket_qua_tra = td.TraTu(tu_can_tra)
print(f"Từ đồng nghĩa của '{tu_can_tra}': {ket_qua_tra['DongNghia']}")
print(f"Từ trái nghĩa của '{tu_can_tra}': {ket_qua_tra['TraiNghia']}")