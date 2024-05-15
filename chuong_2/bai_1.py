def DoiXung(matrix):
    n = len(matrix)
    # Duyệt qua từng hàng của ma trận
    for i in range(n):
        # Duyệt qua từng cột của ma trận
        for j in range(n):
            # Kiểm tra phần tử tại vị trí (i, j) có bằng phần tử tại vị trí (j, i) không
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Ví dụ một ma trận vuông đối xứng
symmetric_matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

# Kiểm tra xem ma trận có đối xứng qua đường chéo chính không
if DoiXung(symmetric_matrix):
    print("Ma trận là ma trận đối xứng qua đường chéo chính.")
else:
    print("Ma trận không phải là ma trận đối xứng qua đường chéo chính.")
