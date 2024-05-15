def pascal_triangle(n):
    # Khởi tạo ma trận tam giác Pascal
    pascal = [[1]]

    # Tính toán các hàng tiếp theo của tam giác Pascal
    for i in range(1, n+1):
        row = [1]  # Phần tử đầu tiên của mỗi hàng luôn là 1

        # Tính toán các phần tử trong hàng hiện tại
        for j in range(1, i):
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        
        row.append(1)  # Phần tử cuối cùng của mỗi hàng luôn là 1
        pascal.append(row)

    # In ra tam giác Pascal
    for row in pascal:
        print(' '.join(map(str, row)))

# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập số nguyên dương n: "))

# In ra tam giác Pascal đến bậc n
pascal_triangle(n)
