import math

# Nhập giá trị của x 
x = float(input("Nhập giá trị của x: "))

# Sử dụng câu điều kiện để đảm bảo x không phải là số âm (vì căn bậc hai)
if x >= 0:
    # Tính tử số: -x + sqrt(x^2 + 4)
    numerator = -x + math.sqrt(x**2 + 4)
    
    # Tính mẫu số: căn bậc 7 của (x^4 + 1)
    denominator = (x**4 + 1)**(1/7)
    
    # Tính f(x)
    f_x = numerator / denominator
    
    # In kết quả, làm tròn đến 2 chữ số thập phân
    print("Giá trị của f(x) là: {:.2f}".format(f_x))
else:
    # In thông báo nếu x là số âm
    print("Giá trị của x phải lớn hơn hoặc bằng 0!")
