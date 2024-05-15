def TamGiacDuoi(matrix):
    n = len(matrix)
    # Duyệt qua từng hàng của ma trận
    for i in range(n):
        # Duyệt qua từng cột của ma trận từ 0 đến i-1
        # Nếu phần tử tại bất kỳ vị trí nào trong khoảng này khác 0, ma trận không phải là tam giác dưới
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True
