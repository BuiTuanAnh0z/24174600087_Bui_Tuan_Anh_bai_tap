# Nhập vào chuỗi ký tự
chuoi = "Hom nay    troi   mua   "
# Tách các từ bằng cách sử dụng split()
cac_tu = chuoi.split()
# Kết hợp lại các từ thành một chuỗi mới (dùng join, yêu cầu của bài)
chuoi_sach = " ".join(cac_tu)
# Đếm số từ trong chuỗi
so_tu = len(cac_tu)

# In ra kết quả
print(f"Số từ trong chuỗi là:{so_tu}")

