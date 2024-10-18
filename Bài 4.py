#Nhập thời gian sử dụng bóng đèn (tính bằng giây)
t= float(input("Nhập thời gian sử dụng bóng đèn(giây): "))
#Các hằng số 
U= 220 #Hiệu điện thế (V)
I= 2.7 #Cường độ dòng điện (A)
gia_dien = 7000 #Giá điện (đ/kwh)
#Tính công suất tiêu thụ của bóng đèn (P=U*I)
P = U*I #Công suất tính bằng Wat
#Tính năng lương tiêu thụ (E=P*t)
E = P*t #Năng lương tiêu thụ tính bằng Joule (Wat-second)
#Đổi năng lượng tiêu thụ sang kWh (1kWh = 1000W * 3600 giây)
E_kWh = E / (1000*3600)
#Tính tiền điện phải trả (T = E_kWh*giá điện)
T = E_kWh * gia_dien
#In kết quả 
print("Tiền điện phải trả là: {:.2f} đ".format(T))
