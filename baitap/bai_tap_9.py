def kiem_tra_chu_va_so(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi chứa toàn chữ và số hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi chứa toàn chữ và số, False nếu không.
    """
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if not (('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z') or ('0' <= ky_tu <= '9')):
            return False
    return True
# Ví dụ 
print(kiem_tra_chu_va_so("Hello123"))  
print(kiem_tra_chu_va_so("Hello@123")) 
print(kiem_tra_chu_va_so("abc123"))   
print(kiem_tra_chu_va_so("abc 123"))   
print(kiem_tra_chu_va_so(""))         
