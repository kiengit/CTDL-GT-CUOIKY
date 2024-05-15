def number_classification(x, y):
    for n in range(x, y + 1):
        # Tính tổng các ước số của n
        divisor_sum = sum([i for i in range(1, n) if n % i == 0])

        # Phân loại số n
        if divisor_sum < n:
            print(f"{n} là deficient")
        elif divisor_sum == n:
            print(f"{n} là perfect")
        else:
            print(f"{n} là abundant")

# Nhập hai số nguyên dương x và y
x = int(input("Nhập số nguyên dương x: "))
y = int(input("Nhập số nguyên dương y (y >= x): "))

# Kiểm tra và in ra phân loại của các số từ x đến y
number_classification(x, y)
