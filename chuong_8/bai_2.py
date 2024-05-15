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

    def DongNghia(self, tu):
        hash_key = tu[0]
        if hash_key in self.tudien and tu in self.tudien[hash_key]:
            return self.tudien[hash_key][tu]['DongNghia']
        else:
            return []

    def TraiNghia(self, tu):
        hash_key = tu[0]
        if hash_key in self.tudien and tu in self.tudien[hash_key]:
            return self.tudien[hash_key][tu]['TraiNghia']
        else:
            return []

# Ví dụ sử dụng
td = TuDien()
td.NhapTu("mèo", ["con mèo", "meo"], ["chó"])
td.NhapTu("chó", ["con chó", "cho"], ["mèo"])
td.NhapTu("vàng", ["màu vàng", "vang"], ["xanh"])

tu_can_tra = "mèo"
tu_dong_nghia = td.DongNghia(tu_can_tra)
tu_trai_nghia = td.TraiNghia(tu_can_tra)
print(f"Từ đồng nghĩa của '{tu_can_tra}': {tu_dong_nghia}")
print(f"Từ trái nghĩa của '{tu_can_tra}': {tu_trai_nghia}")

tu_can_tra = "chó"
tu_dong_nghia = td.DongNghia(tu_can_tra)
tu_trai_nghia = td.TraiNghia(tu_can_tra)
print(f"Từ đồng nghĩa của '{tu_can_tra}': {tu_dong_nghia}")
print(f"Từ trái nghĩa của '{tu_can_tra}': {tu_trai_nghia}")

tu_can_tra = "vàng"
tu_dong_nghia = td.DongNghia(tu_can_tra)
tu_trai_nghia = td.TraiNghia(tu_can_tra)
print(f"Từ đồng nghĩa của '{tu_can_tra}': {tu_dong_nghia}")
print(f"Từ trái nghĩa của '{tu_can_tra}': {tu_trai_nghia}")