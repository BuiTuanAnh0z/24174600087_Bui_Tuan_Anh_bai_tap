# Nhập vào chuỗi ký tự
chuoi = "Hom nay    troi   mua   "
# Tách các từ trong chuỗi
cac_tu = chuoi.split()
# Kết hợp các từ lại thành một chuỗi với dấu cách đúng chuẩn
chuoi_moi = " ".join(cac_tu)
# In kết quả
print(f"Chuỗi sau khi loại bỏ dấu cách thừa:{chuoi_moi}")
