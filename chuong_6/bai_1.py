def Duynhat(a):
    # Tạo một tập hợp từ mảng a để loại bỏ các phần tử trùng lặp
    unique_set = set(a)
    # Sắp xếp các phần tử duy nhất theo thứ tự tăng dần và chuyển thành danh sách
    unique_sorted_list = sorted(unique_set)
    return unique_sorted_list

# Ví dụ sử dụng
a = [1, 5, 3, 7, 5, 9, 7]
result = Duynhat(a)
print("Mảng sau khi loại bỏ phần tử trùng lặp và sắp xếp:", result)