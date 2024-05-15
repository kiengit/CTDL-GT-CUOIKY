def DayConDaiNhat(a, b):
    # Tìm độ dài của mảng a và b
    len_a = len(a)
    len_b = len(b)
    
    # Khởi tạo mảng c để lưu trữ dãy con
    c = []
    
    # Duyệt qua từng phần tử của mảng a
    for i in range(len_a):
        # Nếu phần tử hiện tại của a không tồn tại trong b, bỏ qua
        if a[i] not in b:
            continue
        
        # Nếu phần tử hiện tại của a cũng tồn tại trong b
        # Kiểm tra các phần tử liên tiếp của a có trong b không
        j = i
        k = 0
        temp_c = []
        while j < len_a and k < len_b and a[j] == b[k]:
            temp_c.append(a[j])
            j += 1
            k += 1
        
        # Nếu tìm thấy dãy con mới có độ dài lớn hơn dãy con hiện tại, cập nhật lại mảng c
        if len(temp_c) > len(c):
            c = temp_c
    
    return c
