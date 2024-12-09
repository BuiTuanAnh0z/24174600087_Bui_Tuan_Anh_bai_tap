def kiem_tra_so_thap_phan(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi chứa toàn các ký tự số thập phân hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi chứa toàn số thập phân, False nếu không.
    """
    da_cham = False  # Biến kiểm tra xem đã gặp dấu chấm thập phân hay chưa
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if '0' <= ky_tu <= '9':  # Kiểm tra nếu ký tự là số
            continue
        elif ky_tu == '.' and not da_cham:  # Kiểm tra dấu chấm thập phân, chỉ được có 1 dấu chấm
            da_cham = True
        else:
            return False  # Nếu gặp ký tự không phải số hoặc dấu chấm thập phân, trả về False
    return True
# Ví dụ
print(kiem_tra_so_thap_phan("123.45"))  
print(kiem_tra_so_thap_phan("12345"))  
print(kiem_tra_so_thap_phan("12.34.56"))
print(kiem_tra_so_thap_phan("123a45"))  
print(kiem_tra_so_thap_phan("123.")) 
print(kiem_tra_so_thap_phan("12345."))
