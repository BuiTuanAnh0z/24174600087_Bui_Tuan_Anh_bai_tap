# Nhập năm cần kiểm tra
nam = int(input("Nhập năm cần kiểm tra: "))

# Kiểm tra điều kiện năm nhuận
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(nam, "là năm nhuận.")
else:
    print(nam, "không phải là năm nhuận.")
