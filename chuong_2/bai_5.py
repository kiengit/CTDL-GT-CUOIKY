def Cong(a, b):
    # Chuyển mảng a và b thành chuỗi và sau đó thành số nguyên
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))

    # Tính tổng
    result = num_a + num_b

    # Kiểm tra xem kết quả có bị tràn không
    if result > 999999:
        return [-1] * 6  # Trả về mảng chứa 6 số -1 nếu kết quả bị tràn
    else:
        # Chuyển kết quả thành một mảng các chữ số
        result_digits = [int(digit) for digit in str(result).zfill(6)]
        return result_digits
