def Tru(a, b):
    # Chuyển mảng a và b thành chuỗi và sau đó thành số nguyên
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))

    # Tính hiệu
    result = num_a - num_b

    return result
