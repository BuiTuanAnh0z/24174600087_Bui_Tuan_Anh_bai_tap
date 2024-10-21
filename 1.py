import math 
x = input  ("Nhập giá trị x : ")
x = float (x)
f_x = math.log(x,4) + math.log(2,x)
print (f" Giá trị cần tìm f(x)= {f_x :2f}")