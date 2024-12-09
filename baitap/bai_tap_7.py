def kiem_tra_toan_so(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi chứa toàn số hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu là chuỗi chứa toàn số, False nếu không.
    """
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if not ('0' <= ky_tu <= '9'):  # Kiểm tra nếu ký tự không phải là số
            return False
    return True
# Ví dụ sử dụng
print(kiem_tra_toan_so("12345"))  
print(kiem_tra_toan_so("123a5")) 
print(kiem_tra_toan_so("00123")) 
print(kiem_tra_toan_so("abc"))   
print(kiem_tra_toan_so(""))      