import math

# Nhập giá trị của x 
x = float(input("Nhập giá trị của x: "))

# Sử dụng câu điều kiện để kiểm tra nếu x > 0
if x > 0:
    # Tính log_4(x) = log(x) / log(4)
    log4_x = math.log(x) / math.log(4)
    
    # Tính log_x(2) = log(2) / log(x)
    logx_2 = math.log(2) / math.log(x)
    
    # Tính giá trị của f(x)
    f_x = log4_x + logx_2
    
    # In kết quả, làm tròn đến số thập phân thứ 2
    print("Giá trị của f(x) là: {:.2f}".format(f_x))
else:
    # In thông báo nếu x không hợp lệ
    print("Giá trị của x phải lớn hơn 0!")
