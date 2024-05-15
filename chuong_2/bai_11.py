def Cong(a, b):
    # Tính độ dài của mảng a và b
    len_a = len(a)
    len_b = len(b)
    
    # Xác định độ dài lớn nhất của hai mảng
    max_len = max(len_a, len_b)
    
    # Khởi tạo biến lưu trữ kết quả
    result = []
    
    # Khởi tạo biến nhớ
    carry = 0
    
    # Duyệt qua từng phần tử từ cuối mảng về đầu mảng
    for i in range(max_len - 1, -1, -1):
        # Lấy phần tử cuối cùng của mảng a
        digit_a = a[i] if i >= 0 else 0
        
        # Lấy phần tử cuối cùng của mảng b
        digit_b = b[i] if i >= 0 else 0
        
        # Tính tổng của hai phần tử cộng thêm biến nhớ
        total = digit_a + digit_b + carry
        
        # Nếu tổng lớn hơn 9, lưu phần dư vào biến nhớ
        if total > 9:
            carry = 1
            total -= 10
        else:
            carry = 0
        
        # Thêm phần tử tổng vào mảng kết quả
        result.insert(0, total)
    
    # Nếu còn biến nhớ sau khi đã duyệt hết các phần tử
    # của hai mảng, tức là kết quả bị tràn
    if carry == 1:
        # Trả về mảng gồm các số -1
        return [-1] * (max_len + 1)
    
    # Trả về mảng kết quả
    return result
