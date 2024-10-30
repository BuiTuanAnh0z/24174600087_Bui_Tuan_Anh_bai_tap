# Nhập tọa độ của điểm M
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))

# Nhập tọa độ của tâm hình tròn I và bán kính R
a = float(input("Nhập tọa độ x của tâm I: "))
b = float(input("Nhập tọa độ y của tâm I: "))
R = float(input("Nhập bán kính R của hình tròn: "))

# Tính khoảng cách bình phương từ M đến I
khoang_cach_binh_phuong = (x - a)**2 + (y - b)**2

# Kiểm tra xem điểm M có nằm trong hoặc trên hình tròn hay không
if khoang_cach_binh_phuong <= R**2:
    print("True - Điểm M nằm trong hoặc trên hình tròn.")
else:
    print("False - Điểm M nằm ngoài hình tròn.")
