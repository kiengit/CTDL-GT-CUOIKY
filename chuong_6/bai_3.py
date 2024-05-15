def Giao(a, b):
    # Loại bỏ phần tử trùng lặp và sắp xếp mảng a và b
    unique_a = sorted(set(a))
    unique_b = sorted(set(b))
    
    # Khởi tạo mảng kết quả
    c = []
    
    # Lặp qua từng phần tử trong mảng a
    for num in unique_a:
        # Kiểm tra xem phần tử có tồn tại trong mảng b không
        if num in unique_b:
            # Nếu có, thêm vào mảng kết quả
            c.append(num)
    
    return c

# Ví dụ sử dụng
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Giao(a, b)
print("Mảng c chứa các số có trong cả mảng a và mảng b:", result)
