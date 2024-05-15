def Tru(a, b):
    # Tính độ dài của mảng a và b
    len_a = len(a)
    len_b = len(b)
    
    # Xác định độ dài lớn nhất của hai mảng
    max_len = max(len_a, len_b)
    
    # Khởi tạo biến lưu trữ kết quả
    result = []
    
    # Khởi tạo biến nhớ
    borrow = 0
    
    # Duyệt qua từng phần tử từ cuối mảng về đầu mảng
    for i in range(max_len - 1, -1, -1):
        # Lấy phần tử cuối cùng của mảng a
        digit_a = a[i] if i >= 0 else 0
        
        # Lấy phần tử cuối cùng của mảng b
        digit_b = b[i] if i >= 0 else 0
        
        # Trừ phần tử của mảng b từ phần tử của mảng a cộng với biến nhớ
        # Trừ 1 nếu cần mượn (nếu phần tử của mảng a nhỏ hơn phần tử của mảng b và có biến nhớ)
        diff = digit_a - digit_b - borrow
        
        # Nếu kết quả là số âm, mượn 1 từ phần tử bên trái
        if diff < 0:
            borrow = 1
            diff += 10
        else:
            borrow = 0
        
        # Thêm phần tử hiệu vào mảng kết quả
        result.insert(0, diff)
    
    # Nếu còn biến nhớ sau khi đã duyệt hết các phần tử
    # của hai mảng, tức là kết quả bị tràn
    if borrow == 1:
        # Trả về mảng gồm các số -1
        return [-1] * (max_len + 1)
    
    # Loại bỏ các số 0 ở đầu mảng kết quả nếu có
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    # Trả về mảng kết quả
    return result
