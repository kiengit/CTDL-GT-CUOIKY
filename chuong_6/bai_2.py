def Hieu(a, b):
    # Loại bỏ phần tử trùng lặp và sắp xếp mảng a và b
    unique_a = sorted(set(a))
    unique_b = sorted(set(b))
    
    # Khởi tạo mảng kết quả
    c = []
    
    # Lặp qua từng phần tử trong mảng a
    for num in unique_a:
        # Kiểm tra xem phần tử có tồn tại trong mảng b không
        if num not in unique_b:
            # Nếu không tồn tại, thêm vào mảng kết quả
            c.append(num)
    
    return c

# Ví dụ sử dụng
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Hieu(a, b)
print("Mảng c chứa các số có trong mảng a nhưng không có trong mảng b:", result)
