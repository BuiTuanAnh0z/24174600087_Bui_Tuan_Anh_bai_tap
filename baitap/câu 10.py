import math

# Nhập giá trị vận tốc ban đầu a 
a = float(input("Nhập vận tốc ban đầu của xe (m/s): "))

# Tính log_4(5) bằng cách dùng công thức đổi cơ số logarithm
log4_5 = math.log(5) / math.log(4)

# Tính thời gian t
t = a**4 / log4_5

# In kết quả, làm tròn đến số thập phân thứ 2
print("Thời gian ô tô dừng lại là: {:.2f} giây".format(t))
