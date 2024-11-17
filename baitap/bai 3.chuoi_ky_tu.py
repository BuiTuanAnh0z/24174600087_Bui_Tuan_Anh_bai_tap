# Nhập vào họ tên đầy đủ
ho_ten = "  Vo   Van  Nam  "
# Tách các từ trong chuỗi
cac_tu = ho_ten.split()
# Sử dụng join để tạo lại chuỗi đã loại bỏ khoảng trắng thừa
ho_ten_sach = " ".join(cac_tu)
# Tách họ và tên riêng
ho = cac_tu[0]  # Họ là từ đầu tiên
ten = cac_tu[-1]  # Tên là từ cuối cùng
# In kết quả
print(f"Họ:{ho}")
print(f"Tên:{ten}")
