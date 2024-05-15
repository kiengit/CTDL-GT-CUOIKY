def Hop(a, b):
    # Kết hợp hai mảng a và b, loại bỏ phần tử trùng lặp và sắp xếp mảng kết quả
    combined_array = sorted(set(a + b))
    
    return combined_array

# Ví dụ sử dụng
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Hop(a, b)
print("Mảng c chứa các số có trong cả mảng a và mảng b:", result)

