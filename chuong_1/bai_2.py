def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def neper(n):
    total = 0
    for k in range(n + 1):
        total += 1 / factorial(k)
    return total

# Số nguyên n nhập từ người dùng
n = int(input("Nhập số nguyên không âm n: "))

# Tính và in ra tổng của các số hạng trong dãy Neper
print("Tổng của các số hạng trong dãy Neper:", neper(n))
