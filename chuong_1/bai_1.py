# giải thuật không đệ quy
def fibonacci_iterative(n):
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(2, n+1):
        c = a + b
        a, b = b, c
    return b

# Kiểm tra kết quả
n = int(input("Nhập số nguyên n >= 0: "))
print(f"Số Fibonacci của {n} là: {fibonacci_iterative(n)}")

# giải thuật đệ quy
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Kiểm tra kết quả
n = int(input("Nhập số nguyên n >= 0: "))
print(f"Số Fibonacci của {n} là: {fibonacci_recursive(n)}")
