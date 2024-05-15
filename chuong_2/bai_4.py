def NhomHang(matrix):
    n = len(matrix)
    visited = set()  # Tạo một tập hợp để lưu các chỉ mục hàng đã xem

    for i in range(n):
        if i not in visited:  # Nếu hàng chưa được xem trước đó
            group = [i]  # Khởi tạo một nhóm mới với hàng hiện tại
            visited.add(i)  # Đánh dấu hàng hiện tại đã được xem

            # Duyệt qua các hàng còn lại trong ma trận
            for j in range(i + 1, n):
                # Nếu hàng j giống với hàng i và chưa được xem trước đó
                if matrix[i] == matrix[j] and j not in visited:
                    group.append(j)  # Thêm hàng j vào nhóm
                    visited.add(j)  # Đánh dấu hàng j đã được xem

            # In ra chỉ mục của các hàng trong nhóm
            print("Nhóm hàng:", group)
