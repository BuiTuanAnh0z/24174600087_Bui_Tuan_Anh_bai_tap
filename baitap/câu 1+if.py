# Nhập bán kính và chiều cao 
r = float(input("Nhập bán kính của khối trụ (r): "))
h = float(input("Nhập chiều cao của khối trụ (h): "))

# Pi
pi = 3.14

# Sử dụng câu điều kiện để kiểm tra xem bán kính và chiều cao có hợp lệ hay không
if r > 0 and h > 0:
    # Tính diện tích xung quanh
    Sxq = 2 * pi * r * h

    # Tính diện tích toàn phần
    Stp = 2 * pi * r * (r + h)

    # Tính thể tích
    V = pi * r**2 * h

    # In kết quả, làm tròn đến số thập phân thứ 2
    print("Diện tích xung quanh: {:.2f}".format(Sxq))
    print("Diện tích toàn phần: {:.2f}".format(Stp))
    print("Thể tích: {:.2f}".format(V))
else:
    print("Bán kính và chiều cao phải lớn hơn 0!")
