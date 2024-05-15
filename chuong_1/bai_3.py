# giải thuật không đệ quy
def gcd_iterative(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# Nhập hai số nguyên dương m và n từ người dùng
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

# In ra ước số chung lớn nhất của m và n
print("Ước số chung lớn nhất của", m, "và", n, "là:", gcd_iterative(m, n))

# giải thuật đệ quy
def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)

# Nhập hai số nguyên dương m và n từ người dùng
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

# In ra ước số chung lớn nhất của m và n
print("Ước số chung lớn nhất của", m, "và", n, "là:", gcd_recursive(m, n))
