# Nhập ba số từ bàn phím
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))
so_3 = float(input("Nhập số thứ ba: "))

# Kiểm tra và tìm số lớn nhất
if so_1 >= so_2 and so_1 >= so_3:
    so_lon_nhat = so_1
elif so_2 >= so_1 and so_2 >= so_3:
    so_lon_nhat = so_2
else:
    so_lon_nhat = so_3

# In kết quả
print("Số lớn nhất là:", so_lon_nhat)
