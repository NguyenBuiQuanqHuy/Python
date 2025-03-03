n = int(input("Nhập số nguyên dương n: "))

# Hình 1
print("Hình 1:")
for i in range(n):
    print("* " * n)

print("\nHình 2:")
# Hình 2
for i in range(1, n + 1):
    print("* " * i)

print("\nHình 3:")
# Hình 3
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
for i in range(2, n + 1):
    print(" " * (n - i) + "* " * i)
