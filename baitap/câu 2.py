import math

# Nhập giá trị x 
x = float(input("Nhập giá trị của x: "))

# Tính giá trị của biểu thức
Tu_so  = -x + math.sqrt(x**2 + 4)  
Mau_so = (x**4 + 1)**(1/7)       
f_x = Tu_so / Mau_so         

# In kết quả, làm tròn đến số thập phân thứ 2
print("Giá trị của f(x) là: {:.2f}".format(f_x))
