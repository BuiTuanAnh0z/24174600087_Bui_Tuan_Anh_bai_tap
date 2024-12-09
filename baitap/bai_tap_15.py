def kiem_tra_email(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi hợp lệ của địa chỉ email hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi là một địa chỉ email hợp lệ, False nếu không.
    """
    da_at = False  # Biến kiểm tra xem đã gặp ký tự '@' chưa
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if ('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z') or ('0' <= ky_tu <= '9') or (ky_tu == '.') or (ky_tu == '_'):
            continue  # Nếu ký tự hợp lệ, tiếp tục kiểm tra
        elif ky_tu == '@' and not da_at:  # Chỉ được có một dấu '@'
            da_at = True
        else:
            return False  # Nếu gặp ký tự không hợp lệ, trả về False
    return da_at  # Kết quả trả về True nếu có một dấu '@' trong chuỗi
# Ví dụ
print(kiem_tra_email("example@example.com"))  
print(kiem_tra_email("example@example_com"))  
print(kiem_tra_email("example@com"))        
print(kiem_tra_email("example@.com"))       
print(kiem_tra_email("example.com"))    
print(kiem_tra_email(""))                   
