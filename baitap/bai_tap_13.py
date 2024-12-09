def kiem_tra_chuoi_cho_dau_cach(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi chỉ chứa dấu cách hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi chỉ chứa dấu cách, False nếu không.
    """
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if ky_tu != ' ':  # Nếu gặp ký tự không phải dấu cách
            return False
    return True  # Nếu tất cả các ký tự đều là dấu cách
# Ví dụ
print(kiem_tra_chuoi_cho_dau_cach("     ")) 
print(kiem_tra_chuoi_cho_dau_cach(" hello ")) 
print(kiem_tra_chuoi_cho_dau_cach("    a "))  
print(kiem_tra_chuoi_cho_dau_cach(""))        
