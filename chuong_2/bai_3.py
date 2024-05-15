def TrungHang(matrix):
    n = len(matrix)
    # Duyệt qua từng cặp hàng trong ma trận
    for i in range(n):
        for j in range(i + 1, n):
            # So sánh từng phần tử của hai hàng
            if matrix[i] == matrix[j]:
                return True
    return False