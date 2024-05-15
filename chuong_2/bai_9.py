def TrungCot(matrix):
    n = len(matrix)
    # Duyệt qua từng cột của ma trận
    for j in range(n):
        # Duyệt qua từng cột khác của ma trận để so sánh với cột hiện tại
        for k in range(j + 1, n):
            # So sánh từng phần tử trong hai cột
            for i in range(n):
                if matrix[i][j] != matrix[i][k]:
                    break
            else:
                # Nếu tất cả các phần tử trong hai cột đều giống nhau, trả về True
                return True
    return False
