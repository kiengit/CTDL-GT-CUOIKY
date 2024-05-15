def Nhan(a, b):
    # Chuyển mảng a và b thành chuỗi và sau đó thành số nguyên
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))

    # Tính tích
    result = num_a * num_b

    # Kiểm tra tràn số
    if result > 2**31 - 1:
        return [-1]  # Trả về mảng gồm -1 nếu kết quả bị tràn
    else:
        return result  # Trả về kết quả nếu không bị tràn
