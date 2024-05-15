class BaiHat:
    def __init__(self, ten, nhac_si, ca_si):
        self.ten = ten
        self.nhac_si = nhac_si
        self.ca_si = ca_si

class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.baihats = []

    def ThemBaiHat(self, ten, nhac_si, ca_si):
        baihat = BaiHat(ten, nhac_si, ca_si)
        self.baihats.append(baihat)

class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        album = Album(ten_album)
        for bai_hat in danh_sach_bai_hat:
            ten, nhac_si, ca_si = bai_hat
            album.ThemBaiHat(ten, nhac_si, ca_si)
        self.albums[ten_album] = album

    def XemAlbum(self, ten_album):
        if ten_album in self.albums:
            album = self.albums[ten_album]
            print(f"Album: {album.ten_album}")
            print("Danh sách bài hát:")
            for i, baihat in enumerate(album.baihats, 1):
                print(f"{i}. Tên: {baihat.ten}, Nhạc sĩ: {baihat.nhac_si}, Ca sĩ: {baihat.ca_si}")
        else:
            print("Album không tồn tại.")

# Ví dụ sử dụng
td = TuDien()
td.NhapAlbum("Album A", [("Bài hát 1", "Nhạc sĩ A", "Ca sĩ X"), ("Bài hát 2", "Nhạc sĩ B", "Ca sĩ Y")])
td.NhapAlbum("Album B", [("Bài hát 3", "Nhạc sĩ C", "Ca sĩ Z"), ("Bài hát 4", "Nhạc sĩ D", "Ca sĩ W")])

td.XemAlbum("Album A")
print()
td.XemAlbum("Album B")
print()
td.XemAlbum("Album C")