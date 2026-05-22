tong = 0
while True:
    n = int(input("Nhap n, 0 de dung: "))
    if n == 0:
        break
    if n % 2 == 0:
        tong += n
print(tong)
