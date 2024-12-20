import math

# Nhập giá trị x 
x = float(input("Nhập giá trị của x: "))

# Tính giá trị của biểu thức f(x)
log4_x = math.log(x) / math.log(4)  # Tính log_4(x)
logx_2 = math.log(2) / math.log(x)  # Tính log_x(2)
f_x = log4_x + logx_2  # Tổng của log_4(x) và log_x(2)

# In kết quả, làm tròn đến số thập phân thứ 2
print("Giá trị của f(x) là: {:.2f}".format(f_x))
