def Dao(matrix):
    # Hàm tính diện tích lớn nhất của các đảo có dạng hình chữ nhật
    def findMaxRectArea(hist):
        stack = []
        max_area = 0
        index = 0
        while index < len(hist):
            if (not stack) or (hist[index] >= hist[stack[-1]]):
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (hist[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)
        while stack:
            top_of_stack = stack.pop()
            area = (hist[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
        return max_area

    # Hàm chuyển đổi ma trận sang dạng histogram
    def toHistogram(row):
        hist = [0] * len(row)
        for i in range(len(row)):
            if i == 0:
                hist[i] = 1 if row[i] == 1 else 0
            else:
                hist[i] = hist[i-1] + 1 if row[i] == 1 else 0
        return hist

    # Khởi tạo biến để lưu diện tích lớn nhất của các đảo
    max_area = 0

    # Duyệt qua từng hàng trong ma trận
    for row in matrix:
        # Chuyển đổi hàng hiện tại thành histogram
        hist = toHistogram(row)
        # Tính diện tích lớn nhất của các đảo có dạng hình chữ nhật trên hàng hiện tại
        max_area = max(max_area, findMaxRectArea(hist))

    return max_area

# Ma trận mẫu
matrix = [
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

# In ra diện tích lớn nhất của các đảo có dạng hình chữ nhật trong ma trận
print("Diện tích lớn nhất của các đảo có dạng hình chữ nhật trong ma trận là:", Dao(matrix))
