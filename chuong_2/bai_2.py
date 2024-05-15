def TamGiacTren(matrix):
    n = len(matrix)
    # Duyệt qua từng hàng của ma trận
    for i in range(n):
        # Duyệt qua từng cột của ma trận từ i+1 đến n-1
        # Nếu phần tử tại bất kỳ vị trí nào trong khoảng này khác 0, ma trận không phải là tam giác trên
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False
    return True

# Ví dụ một ma trận vuông tam giác trên
upper_triangular_matrix = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

# Kiểm tra xem ma trận có phải là ma trận tam giác trên không
if TamGiacTren(upper_triangular_matrix):
    print("Ma trận là ma trận tam giác trên.")
else:
    print("Ma trận không phải là ma trận tam giác trên.")

