def Cong(a, b):
    # Tính độ dài của mảng a và b
    len_a = len(a)
    len_b = len(b)
    
    # Lưu trữ kết quả vào một mảng mới
    result = []
    
    # Khởi tạo biến nhớ
    carry = 0
    
    # Duyệt qua từng phần tử từ cuối mảng về đầu mảng
    for i in range(max(len_a, len_b) - 1, -1, -1):
        # Lấy giá trị tương ứng từ mảng a và b (nếu có)
        val_a = a[i] if i < len_a else 0
        val_b = b[i] if i < len_b else 0
        
        # Cộng hai giá trị và biến nhớ
        temp = val_a + val_b + carry
        result.insert(0, temp % 10)
        carry = temp // 10
    
    # Nếu vẫn còn biến nhớ sau khi đã duyệt hết các phần tử của mảng
    if carry:
        result.insert(0, carry)
    
    # Trả về mảng kết quả
    return result


def Nhan(a, b):
    # Tính độ dài của mảng a và b
    len_a = len(a)
    len_b = len(b)
    
    # Khởi tạo biến lưu trữ kết quả
    result = []
    
    # Khởi tạo biến nhớ
    carry = 0
    
    # Duyệt qua từng phần tử từ cuối mảng về đầu mảng của b
    for i in range(len_b - 1, -1, -1):
        # Khởi tạo một mảng tạm thời để lưu trữ phần tử của kết quả của lần nhân
        temp_result = [0] * (len_a + len_b)
        # Khởi tạo biến nhớ cho lần nhân
        carry = 0
        
        # Duyệt qua từng phần tử từ cuối mảng về đầu mảng của a
        for j in range(len_a - 1, -1, -1):
            # Nhân hai phần tử tương ứng và cộng vào vị trí thích hợp trong mảng tạm thời
            temp = a[j] * b[i] + carry
            temp_result[i + j + 1] = temp % 10
            carry = temp // 10
        
        # Nếu vẫn còn biến nhớ sau khi đã duyệt hết các phần tử của mảng a
        if carry:
            temp_result[i] += carry
        
        # Cộng mảng tạm thời vào mảng kết quả
        result = Cong(result, temp_result)
    
    # Loại bỏ các số 0 ở đầu mảng kết quả nếu có
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    # Trả về mảng kết quả
    return result
