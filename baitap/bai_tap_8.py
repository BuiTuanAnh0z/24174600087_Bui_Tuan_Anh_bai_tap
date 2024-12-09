def kiem_tra_toan_chu(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi chứa toàn chữ cái hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi chứa toàn chữ cái, False nếu không.
    """
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if not (('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z')):  # Kiểm tra nếu ký tự không phải là chữ cái
            return False
    return True
# Ví dụ 
print(kiem_tra_toan_chu("Hello"))   
print(kiem_tra_toan_chu("Hello123"))  
print(kiem_tra_toan_chu("abc"))    
print(kiem_tra_toan_chu("abc123"))
print(kiem_tra_toan_chu(""))        
