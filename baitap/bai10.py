# Nhập lương nhân viên từ bàn phím
luong = float(input("Nhập lương nhân viên (đồng): "))

# Tính thuế thu nhập và lương ròng
if luong > 15000000:
    thue = luong * 0.3  # 30% thuế
elif 7000000 <= luong <= 15000000:
    thue = luong * 0.2  # 20% thuế
else:
    thue = luong * 0.1  # 10% thuế

# Tính lương ròng
luong_rong = luong - thue

# In kết quả
print(f"Lương nhân viên: {luong:.0f} đồng")
print(f"Thuế thu nhập: {thue:.0f} đồng")
print(f"Lương ròng (lương thực nhận): {luong_rong:.0f} đồng")
