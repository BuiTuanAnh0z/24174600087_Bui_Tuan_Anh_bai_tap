def kiem_tra_ky_tu_dac_biet(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi chứa ký tự đặc biệt hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi chứa ký tự đặc biệt, False nếu không.
    """
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if not (('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z') or ('0' <= ky_tu <= '9')):
            return True  # Nếu ký tự không phải là chữ cái hoặc chữ số, tức là ký tự đặc biệt
    return False  # Nếu không có ký tự đặc biệt nào
# Ví dụ 
print(kiem_tra_ky_tu_dac_biet("Hello123!"))  
print(kiem_tra_ky_tu_dac_biet("Hello123"))    
print(kiem_tra_ky_tu_dac_biet("abc@123"))    
print(kiem_tra_ky_tu_dac_biet("abc123"))     
print(kiem_tra_ky_tu_dac_biet(""))
