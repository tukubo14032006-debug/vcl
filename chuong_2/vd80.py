t = float(input("Nhập điểm Toán: "))
l = float(input("Nhập điểm Lý: "))
h = float(input("Nhập điểm Hóa: "))

tb = (t + l + h) / 3
print("Điểm trung bình:", tb)

if tb < 5:
    print("Yếu")
elif tb < 7:
    print("Trung bình")
elif tb < 9:
    print("Khá")
else:
    print("Giỏi")
